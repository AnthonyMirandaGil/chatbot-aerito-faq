
from typing import Any, Text, Dict, List

from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet, EventType, UserUtteranceReverted, ConversationPaused
from rasa_sdk.executor import CollectingDispatcher

import logging

logger = logging.getLogger(__name__)

#class ActionTriggerResponseSelector(Action):
#    """Returns the chitchat utterance dependent on the intent"""
#
#    def name(self) -> Text:
#        return "action_trigger_response_selector"
#
#    def run(
#        self,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> List[EventType]:
#        retrieval_intent = tracker.get_slot("retrieval_intent")
#        print('retrieval_intent:', retrieval_intent)
#        if retrieval_intent:
#            dispatcher.utter_message(response = f"utter_{retrieval_intent}")
#        
#        return [SlotSet("retrieval_intent", None)]


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
            "matricula__procedimiento_alumno_regular": 'Cuál es el proceso de matrícula para un alumno regular?',
            "matricula__procedimiento_alumno_ingresante":"¿Cuál es el proceso de matrícula para un alumno ingresante?",
            "carnet_universitario__solicitud":"¿Cómo obtener mi carnet universitario?",
            "matricula__cronograma":"¿Cuando es la matrícula?",
            "matricula__horarios":"¿Cuál es mi horario de matrícula?",
            "pago_autoseguro__fechas":"¿Cuando se puede pagar el autoseguro?",
            "pago_autoseguro_procedimiento":"¿Como realizo el pago de autoseguro?",
            "pago_autoseguro__fuera_fecha":"¿Que sucede si demore en realizar el pago de autoseguro?",
            "perdida_turno_matricula":"¿Como puedo matricularme si perdí mi turno de matricula?",
            "matricula_rezagada__procedimiento":"¿Cuál es el procedimiento para la matricula rezagada?",
            "cambio_seccion":"¿Cuál es procedimiento para hacer un cambio de sección?",
            "cursos_horarios":"¿Donde puedo ver los horarios de los cursos de este ciclo?",
            "retiro_parcial__fechas":"¿En que semana se realiza el retiro parcial?",
            "retiro_parcial__procedimiento":"¿Cómo realizo un retiro parcial?",
            "retiro_parcial__unico_curso":"¿El retiro parcial aplica para los estudiantes que llevan solo un curso?",
            "retiro_parcial__maximo_cursos":"¿Cuantos cursos es el máximo que puedo retirarme?",
            "retiro_total__fechas":"¿En que fecha se realiza el retiro total?",
            "retiro_total__requisitos_documentos_justificacion":"¿Es necesario justificar con documentos el motivo de retiro total?",
            "retiro_total__motivos_procede":"¿Cuáles son los motivos para acceder al retiro total?",
            "retiro_total__formato_solicitud":"¿Cuál es el modelo para la solicitud de retiro total?",
            "retiro_total__procedimiento":"¿Cómo hago el retiro total de mis cursos?",
            "reserva_matricula__procedimiento":"¿Cómo reservo mi matricula?",
            "reserva_matricula__fechas":"¿Hasta que dias puedo enviar la solicitud de reserva de matricula ?C",
            "reserva_matricula__formato_solicitud":"¿Cuál es el modelo de solicitud para la reserva de matricula?",
            "reincorporacion__procedimiento":"¿Cuál es el procedimiento para solicitar reincorporación?",
            "reincorporacion_rezagada__procedimiento":"Si ya pasaron las fechas de reincoporacion, ¿Puedo enviar mi solicitud de reincoporacion?",
            "reincorporacion__fechas":"¿Hasta cuando enviar mi solicitud de reincorporacion?",
            "reincorporacion__costo":"¿Cuánto se paga por el tramite de reincorporación?",
            "reincorporacion__formato_solicitud":"¿Hay un modelo para la solicitud de reincorporación?",
            "constancia_matricula__solicitud_procedimiento":"¿Cómo puedo obtener una constancia de matricula?",
            "constancia_matricula__pago":"¿Cuánto se paga por la Constancia de Matrícula?",
            "constancia_matricula__formato_solicitud":"¿Hay un modelo para la solicitud de constancia de matricula?",
            "constancia_de_notas__procedimiento":"¿Como solicitar una constancia de notas?",
            "constancia_de_notas__formato_solicitud":"¿Hay algun modelo para la solicitud de constancia de notas?",
            "constancia_de_estudios__formato_solicitud":"¿Hay algún modelo para la solicitud de constancia de estudios?",
            "constancia_de_estudios__procedimiento":"¿Cómo solicitar una constancia de estudios?",
            "horario_atencion_aera":"¿Cuál es el horario de AERA?",
            "solicitud_correo_institucional_procedimiento":"¿Cómo solicito mi correo UNI?",
            "retiro_parcial__cursos_repetidos": "¿Es posible retirarme de un curso que haya repetido?",
            'formato_solicitud': "¿Cuál es el modelo para la solicitud?"

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


#class ActionContextualFaqsFormatoSolicitud(Action):
#    """Returns the chitchat utterance dependent on the intent"""
#
#    def name(self) -> Text:
#        return "action_contextual_faq_formato_solicitud"

#    def run(
#        self,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> List[EventType]:
#        sub_topic = tracker.get_slot("sub_topic")
#        print(sub_topic, 'sub_topic')
#        if sub_topic in ["retiro_total", "reincorporacion", "reserva_matricula","constancia_de_estudios","constancia_matricula"]:
#            dispatcher.utter_message(response=f"utter_{sub_topic}__formato_solicitud")
#        else:
#            dispatcher.utter_message(text="Lo lamento no tengo esa información")#
#
#        return []


#class ActionSetSubTopicSlot(Action):
#    """Returns the chitchat utterance dependent on the intent"""
#
#    def name(self) -> Text:
#        return "action_set_sub_topic_slot"
#
#    def run(
#        self,
#       dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> List[EventType]:
#        full_intent = (
#            tracker.latest_message.get("response_selector", {})
#            .get("faq", {})
#            .get("response",{})
#            .get("intent_response_key")
#        )
#        print('full_intent:', full_intent)
#        if full_intent:
#            topic = full_intent.split("/")[1]
#            print('topic: ', topic)
#            sub_topic = topic.split("__")[0]
#        else:
#            sub_topic = None
#        print('sub_topic:', sub_topic)
#        return [SlotSet("sub_topic", sub_topic)]