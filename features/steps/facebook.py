from behave import *

from actions.Action import Actions


@given('website "{url}"')
def step(context, url):
    context.actions = Actions("Chrome")
    context.actions.open_page(url)


@then('login as "{username}" password "{password}"')
def step(context, username, password):
    context.actions.login(username, password)


@then('make random actions')
def step(context):
    context.actions.random_actions()


@then("exit")
def step(context):
    context.actions.exit()
