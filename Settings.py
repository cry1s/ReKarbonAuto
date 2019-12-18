imports = [
    "import pyautogui as pa",
    "from time import sleep"
]

categories = [
    'Клавиатура',
    'Мышь',
    'Ждать',
    'Зациклить',
    'Строка Python',
]

names = [
    ['Нажать', 'Написать', 'Зажать клавишу', 'Разжать клавишу', 'Сочетание клавиш', ],
    ['Передвинуть в', 'Тащить в', 'Кликнуть', 'Зажать', 'Отжать', 'Колесико', ],
    [None],
    ['Открыть', 'Закрыть', ],
    [None],
]

commands = [
    ['pa.press({})', 'pa.typewrite({})', 'pa.keyDown({})', 'pa.keyUp({})', 'pa.hotkey({})'],
    ['pa.moveTo({})', 'pa.dragTo({})', 'pa.click({})', 'pa.mouseDown({})', 'pa.mouseUp({})', 'pa.scroll({})'],
    ['sleep(int({}))'],
    ['for {} in range(int({})):', 'endfor'],
    ['{}'],
]

attributes = [
    [
        'keys, presses=1, interval=0.0, pause=None, logScreenshot=None',
        'message, interval=0.0, pause=None, logScreenshot=None',
        'key, pause=None, logScreenshot=None',
        'key, pause=None, logScreenshot=None',
        '',
    ],
    [
        'x=None, y=None, duration=0.0, tween=linear, pause=None, logScreenshot=False',
        'x=None, y=None, duration=0.0, tween=linear, button=PRIMARY, pause=None, logScreenshot=None'
        'mouseDownUp=True',
        'x=None, y=None, clicks=1, interval=0.0, button=PRIMARY, duration=0.0, tween=linear'
        'logScreenshot=None, _pause=True',
        'x=None, y=None, button=PRIMARY, duration=0.0, tween=linear, pause=None, logScreenshot=None',
        'x=None, y=None, button=PRIMARY, duration=0.0, tween=linear, pause=None, logScreenshot=None',
        'clicks, x=None, y=None, pause=None, logScreenshot=None',
    ],
    ['Количество повторов=3',
     ''],
    ['', '', ],
    ['', ],
]
