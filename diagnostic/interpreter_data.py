from rasa.cli.utils import get_validated_path
from rasa.model import get_model, get_model_subdirectories
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.shared.nlu.constants import TEXT
from rasa.shared.nlu.training_data.message import Message
import pathlib

YOUR_RASA_MODEL_DIRECTORY = '../models'
YOUR_RASA_MODEL_NAME = '20220301-200633'

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
for p in interpreter.interpreter.pipeline:
    p.process(msg)
    print(msg.as_dict())

print(msg)
dict_nlu = msg.as_dict_nlu()
features = msg.get_all_features(TEXT)
dense_sequence_features, dense_sentence_features  = msg.get_dense_features(TEXT)
sparse_sequence_features, sparse_sentence_features = msg.get_sparse_features(TEXT)
sparse_feature_sizes = msg.get_sparse_feature_sizes(TEXT)

print('------------------------------------------')
print("dict_nlu keys:", dict_nlu.keys())
print("diagnostic_data keys:", dict_nlu['diagnostic_data'].keys())
print('features: ', features)
if not dense_sequence_features is None and not dense_sentence_features is None:
    print('dense_sequence_features: ', dense_sequence_features.features.shape)  
    print('dense_sentence_features: ', dense_sentence_features.features.shape)

if not sparse_sequence_features is None and not sparse_sentence_features is None:
    print('sparse_sequence_features: ', sparse_sequence_features.features.shape)
    print('sparse_sentence_features: ', sparse_sequence_features.features.shape)