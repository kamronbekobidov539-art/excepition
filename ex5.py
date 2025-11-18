from translate import Translator

translator = Translator(from_lang="uz", to_lang="en")

data = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]

natija = {}

for item in data:
    if type(item) == str:
        eng = translator.translate(item)
        natija[item] = eng

print(natija)
