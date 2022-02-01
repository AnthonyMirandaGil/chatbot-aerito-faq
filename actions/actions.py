
from typing import Any, Text, Dict, List

from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet, EventType, UserUtteranceReverted, ConversationPaused
from rasa_sdk.executor import CollectingDispatcher

import logging

logger = logging.getLogger(__name__)

class ActionTriggerResponseSelector(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_trigger_response_selector"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        retrieval_intent = tracker.get_slot("retrieval_intent")
        print('retrieval_intent:', retrieval_intent)
        if retrieval_intent:
            dispatcher.utter_message(response = f"utter_{retrieval_intent}")
        
        return [SlotSet("retrieval_intent", None)]


class ActionTriggerMenuAnterior(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_trigger_menu_anterior"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        topic = tracker.get_slot("topic")
        print('topic:', topic)
        if topic:
            dispatcher.utter_message(response = f"utter_formulario_{topic}")
        
        return []
class ActionDefaultAskAffirmation(Action):
    def name(self):
            return "action_default_ask_affirmation"
    
    async def run(self, dispatcher, tracker, domain):
        # select the top three intents from the tracker        
        # ignore the first one -- nlu fallback
        ## usar response_selector
        # A prompt asking the user to select an option
        best_intent = tracker.latest_message["intent_ranking"][1]['name']
        message = "Quisiste decir,"
        if best_intent == 'faq':
            sub_intent = tracker.latest_message['response_selector']['faq']['ranking'][0]['intent_response_key']
            best_intent = sub_intent
            message = "Deseas saber,"

        # a mapping between intents and user friendly wordings
        intent_mappings = {
            "despedida": "Adios",
            "saludo": "Hola",
            "agradecimiento": "Gracias",
            "ayuda": "ayuda",
            "matricula_procedimiento": '¿Cuál es proceso de matricula?',
            "faq/matricula_procedimiento_alumno_regular": 'Cuál es el proceso de matrícula para un alumno regular?',
            "faq/matricula_procedimiento_alumno_ingresante":"¿Cuál es el proceso de matrícula para un alumno ingresante?",
            "faq/solicitud_carnet_universitario":"¿Cómo obtener mi carnet universitario?",
            "faq/matricula_cronograma":"¿Cuando es la matrícula?",
            "faq/matricula_horarios":"¿Cuál es mi horario de matrícula?",
            "faq/matricula_pago_autoseguro_fechas":"¿Cuando se puede pagar el autoseguro?",
            "faq/pago_autoseguro":"¿Como realizo el pago de autoseguro?",
            "faq/matricula_pago_autoseguro_fuera_fecha":"¿Que sucede si demore en realizar el pago de autoseguro?",
            "faq/matricula_rezagada_procedimiento":"¿Cuál es el procedimiento para la matricula rezagada?",
            "faq/cambio_seccion":"¿Cuál es procedimiento para hacer un cambio de sección?",
            "faq/cursos_horarios":"¿Donde puedo ver los horarios de los cursos de este ciclo?",
            "faq/retiro_parcial_fechas":"¿En que semana se realiza el retiro parcial?",
            "faq/retiro_parcial_procedimiento":"¿Cómo realizo un retiro parcial?",
            "faq/retiro_parcial_unico_curso":"¿El retiro parcial aplica para los estudiantes que llevan solo un curso?",
            "faq/retiro_parcial_maximo_cursos":"¿Cuantos cursos es el máximo que puedo retirarme?",
            "faq/retiro_total_fechas":"¿En que fecha se realiza el retiro total?",
            "faq/retiro_total_requisitos_documentos_justificacion":"¿Es necesario justificar con documentos el motivo de retiro total?",
            "faq/motivos_procede_retiro_total":"¿Cuáles son los motivos para acceder al retiro total?",
            "faq/formato_solicitud_retiro_total":"¿Cuál es el modelo para la solicitud de retiro total?",
            "faq/retiro_total_procedimiento":"¿Cómo hago el retiro total de mis cursos?",
            "faq/reserva_matricula_procedimiento":"¿Cómo reservo mi matricula?",
            "faq/reserva_matricula_fechas":"¿Hasta que dias puedo enviar la solicitud de reserva de matricula ?C",
            "faq/formato_solicitud_reserva_matricula":"¿Cuál es el modelo de solicitud para la reserva de matricula?",
            "faq/reincorporacion_procedimiento":"¿Cuál es el procedimiento para solicitar reincorporación?",
            "faq/reincorporacion_rezagada_procedimiento":"Si ya pasaron las fechas de reincoporacion, ¿Puedo enviar mi solicitud de reincoporacion?",
            "faq/reincorporacion_fechas":"¿Hasta cuando enviar mi solicitud de reincorporacion?",
            "faq/reincorporacion_costo":"¿Cuánto se paga por el tramite de reincorporación?",
            "faq/formato_solicitud_reincorporacion":"¿Hay un modelo para la solicitud de reincorporación?",
            "faq/solicitud_constancia_matricula_procedimiento":"¿Cómo puedo obtener una constancia de matricula?",
            "faq/constancia_matricula_pago":"¿Cuánto se paga por la Constancia de Matrícula?",
            "faq/formato_solicitud_constancia_matricula":"¿Hay un modelo para la solicitud de constancia de matricula?",
            "faq/constancia_notas_procedimiento":"¿Como solicitar una constancia de notas?",
            "faq/formato_solicitud_constancia_de_notas":"¿Hay algun modelo para la solicitud de constancia de notas?",
            "faq/formato_solicitud_constancia_estudios":"¿Hay algún modelo para la solicitud de constancia de estudios?",
            "faq/constancia_de_estudios_procedimiento":"¿Cómo solicitar una constancia de estudios?",
            "faq/horario_atencion_aera":"¿Cuál es el horario de AERA?",
            "faq/solicitud_correo_institucional_procedimiento":"¿Cómo solicito mi correo UNI?",
            "faq/retiro_parcial_cursos_repetidos": "¿Es posible retirarme de un curso que haya repetido?"

        }
        
        title_intent = intent_mappings[best_intent]
        buttons = [
            {
                "title": 'Si',
                "payload": "/{}".format(best_intent)
            },
            {
            "title": "No",
            "payload": "/out_of_scope"
            }
        ]
        message = message + ' ' + title_intent 
        
        dispatcher.utter_message(text=message, buttons=buttons)

        return []

class ActionDefaultFallback(Action):
    
    def name(self) -> Text:
        return "action_default_fallback"
    
    def run(self, dispatcher, tracker, domain):
    
        dispatcher.utter_message(text="Lo lamento, no puedo ayudarte con eso.")
        dispatcher.utter_message(text="Recuerda que puedes escribir 'ayuda' para guiarte para guiarte en las principales temas y consultas sobre los cuales puedo responder")
        dispatcher.utter_message(response=f"utter_sugerir_contactar_aera")
        dispatcher.utter_message(response=f"utter_requerir_mas")

        return [ConversationPaused(), UserUtteranceReverted()]


class ActionContextualFaqsFormatoSolicitud(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_contextual_faq_formato_solicitud"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        sub_topic = tracker.get_slot("sub_topic")

        if sub_topic in ["retiro_parcial", "retiro_total", "reincorporacion", "reserva_matricula"]:
            dispatcher.utter_message(response=f"utter_faq_{sub_topic}_formato_solicitud")
        else:
            dispatcher.utter_message(text=="Lo lamento no tengo esa información")

        return []


class ActionSetSubTopicSlot(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_set_sub_topic_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        full_intent = (
            tracker.latest_message.get("response_selector", {})
            .get("sub_topic", {})
            .get("full_retrieval_intent")
        )
        if full_intent:
            topic = full_intent.split("/")[1]
            sub_topic = topic.split("__")[0]
        else:
            sub_topic = None

        return [SlotSet("sub_topic", sub_topic)]