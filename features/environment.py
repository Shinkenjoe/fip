from splinter import Browser


def before_all(context):
    server_url = context.get_url()

    
def before_scenario(context, scenario):
    context.b = Browser()
    context.browsers = {'Edith': 'b', }

    
def after_scenario(context, scenario):
    for b in context.browsers:
        getattr(context, context.browsers[b]).quit()
