from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.web.models.constants import HookActions

from .abstract import TimeStampModel


class Update(TimeStampModel):
    bot = models.ForeignKey(
        to='Bot',
        verbose_name=_('Bot from'),
        on_delete=models.CASCADE,
    )
    update_id = models.BigIntegerField(
        verbose_name=_('Update Id'),
        db_index=True,
    )
    message = models.ForeignKey(
        to='Message',
        related_name='updates',
        verbose_name=_('Message ID'),
        help_text=_('Update action for particular massage'),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    callback_query = models.ForeignKey(
        to='CallbackQuery',
        related_name='updates',
        verbose_name=_('Callback Query'),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Update')
        verbose_name_plural = _('Updates')

    def __str__(self):
        return f'{self.id}'

    @property
    def get_message(self):
        if self.message:
            return self.message
        if self.callback_query:
            return self.callback_query.message
        raise AttributeError

    @property
    def get_sender(self):
        if self.message:
            return self.message.from_user
        if self.callback_query:
            return self.callback_query.from_user
        raise AttributeError

    @property
    def is_reply_button(self):
        message = self.get_message
        keyboard = message.chat.current_keyboard

        if keyboard and (f'\'{message.text}\'' in keyboard):
            return True
        else:
            return False

    @property
    def action_type(self):
        if self.is_reply_button:
            return HookActions.REPLY_BUTTON
        if self.callback_query:
            return HookActions.CALLBACK
        if self.get_message.text and self.get_message.text.startswith('/'):
            return HookActions.COMMAND
        if self.message:
            return HookActions.MESSAGE
