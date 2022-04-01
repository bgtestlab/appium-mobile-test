import os


class AppiumConfigs:
    BASE_SERVER_PORT = "4723"
    BASE_SERVER_URI = f"http://localhost:{BASE_SERVER_PORT}/wd/hub"


class AppConfigs:
    BASE_APP_PATH = "~/Downloads"
    ANDROID_TARGET_APP_NAME = "ApiDemos-debug.apk"
    DESIRED_CAPABILITIES = {
        "device1": {
            "app": os.path.join(
                os.path.expanduser(BASE_APP_PATH), ANDROID_TARGET_APP_NAME
            ),
            "platformName": "Android",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.ApiDemos",
        }
    }
