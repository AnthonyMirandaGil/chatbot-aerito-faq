from rasa.cli.utils import get_validated_path
from rasa.model import get_model, get_model_subdirectories
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.shared.nlu.constants import TEXT
from rasa.shared.nlu.training_data.message import Message
import pathlib
from tensorflow.keras.utils import plot_model


YOUR_RASA_MODEL_DIRECTORY = '../models'
YOUR_RASA_MODEL_NAME = 'ic_diet_ligth'

def load_interpreter(model_dir, model):
    path_str = str(pathlib.Path(model_dir) / model)
    model = get_validated_path(path_str, "model")
    model_path = get_model(model)
    _, nlu_model = get_model_subdirectories(model_path)
    return RasaNLUInterpreter(nlu_model)

    
# Loads the model
interpreter = load_interpreter(YOUR_RASA_MODEL_DIRECTORY, f"{YOUR_RASA_MODEL_NAME}.tar.gz")
# Parses new text
msg = Message({TEXT: "cuando sera la matricula?"})
#for p in interpreter.interpreter.pipeline:
#    p.process(msg)
    #print(msg.as_dict())
print('DIET', interpreter.interpreter.pipeline[3].model)
plot_model(interpreter.interpreter.pipeline[3].model, to_file='DIETClassifier.png')
print('Response Selector', interpreter.interpreter.pipeline[4].model)
plot_model(interpreter.interpreter.pipeline[4].model, to_file='ResponseSelector.png')

