from phonenumber_field.modelfields import PhoneNumberField
from mirage.fields import EncryptedMixin
from django_cpf_cnpj.fields import CPFField


class EncryptedPhonenumberField(EncryptedMixin, PhoneNumberField):
    prepared_max_length = 254


class EncryptedCPFFIeld(EncryptedMixin, CPFField):
    prepared_max_length = 254
