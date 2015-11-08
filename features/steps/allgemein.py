import pytest
import regex as re
import splinter


@given(u'(\w*) besucht die Eingangsseite')
def besuche_eingangsseite(context):
    context.b.visit(server_url)

    
@when(u'Edith zur Eingabeseite wechselt')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Edith zur Eingabeseite wechselt')

@then(u'erscheint ein Formular mit Eingabeboxen mit der ID "Feld"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then erscheint ein Formular mit Eingabeboxen mit der ID "Feld"')

