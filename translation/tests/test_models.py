from django.test import TestCase
from translation.models import TranlastionObject

class TranslationObjectModelTest(TestCase):
    def setUp(self):
        self.translation = TranlastionObject.objects.create(
            InputText="Hello",
            OutputText="Hola",
            FromUser="User1"
        )

    def test_translation_object_str_method(self):
        self.assertEqual(str(self.translation), str(self.translation.pk))

    def test_translation_object_input_text_field(self):
        self.assertEqual(self.translation.InputText, "Hello")

    def test_translation_object_output_text_field(self):
        self.assertEqual(self.translation.OutputText, "Hola")

    def test_translation_object_from_user_field(self):
        self.assertEqual(self.translation.FromUser, "User1")