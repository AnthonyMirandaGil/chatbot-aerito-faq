from rasa.cli.utils import get_validated_path
from rasa.model import get_model, get_model_subdirectories
from rasa.nlu.model import Interpreter
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import TEXT
from rasa.shared.constants import DIAGNOSTIC_DATA
import pathlib
import numpy as np

YOUR_RASA_MODEL_DIRECTORY = './models'
YOUR_RASA_MODEL_NAME = '20220105-180228'

def load_interpreter(model_dir, model):
    path_str = str(pathlib.Path(model_dir) / model)
    model = get_validated_path(path_str, "model")
    model_path = get_model(model)
    _, nlu_model = get_model_subdirectories(model_path)
    return Interpreter.load(nlu_model)


if __name__ == "__main__":
    interpreter = load_interpreter(YOUR_RASA_MODEL_DIRECTORY, f"{YOUR_RASA_MODEL_NAME}.tar.gz")
    data = interpreter.default_output_attributes()
    data[TEXT] = "Hola como estas"
    message = Message(data=data)
    print(interpreter.pipeline)
    for i , e in enumerate(interpreter.pipeline):
        e.process(message)
        featurizer = e
        if i ==2:
            break
    tokens = message.get('text_tokens')
    print('message:', message.as_dict_nlu())
    word_vectors = np.array([featurizer.model.get_word_vector(t.text) for t in tokens])
    print('word_vectors',word_vectors)
    #nlu_diagnostic_data = message.as_dict()[DIAGNOSTIC_DATA]
    #print('message.as_dict_nlu()',  message.as_dict_nlu())
    #print('DIAGNOSTIC_DATA',DIAGNOSTIC_DATA)
    #print('text_tokens', message.as_dict_nlu()['text_tokens'])
    #for component_name, diagnostic_data in nlu_diagnostic_data.items():
        #print(diagnostic_data.keys())
        #print(f"attention_weights for {component_name}:")
    #    attention_weights = diagnostic_data["attention_weights"]
        #print(attention_weights)

        #print(f"\ntext_transformed for {component_name}:")
     #   text_transformed = diagnostic_data["text_transformed"]
        #print(text_transformed)