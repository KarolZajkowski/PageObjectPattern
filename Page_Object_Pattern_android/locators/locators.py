class App:
    whatsApplicationPackage = "com.whatsapp/.HomeActivity"
    youtube = "com.google.android.youtube/.HomeActivity"
    messenger = "com.facebook.orca/.auth.StartScreenActivity"
    Gmail = "com.google.android.gm/.ConversationListActivityGmail"
    Music = "com.android.mediacenter/.PageActivity"
    Maps = "com.google.android.apps.maps/com.google.android.maps.MapsActivity"
    Chrome = "com.android.chrome/com.google.android.apps.chrome.Main"


class KeysInput:
    """" https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8 """
    home = "adb -s {} shell input keyevent KEYCODE_HOME"
    NotificationBar = "adb -s {} shell cmd statusbar expand-notifications"
    swipe = "adb -s {} shell input touchscreen swipe 500 1385 500 785"
    terminate_app = 'adb -s {} shell am force-stop "{}"'
    reboot = 'adb -s {} reboot'


class WhatsApp:
    camera = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]'
    chats = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]'
    status = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]'
    calls = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.TextView'
    buttonCall = '//android.widget.ImageButton[@content-desc="New call"]'


class PhoneAppLocators:
    phone_tab = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView'
    phone_ADDnumber = '//android.widget.FrameLayout[@content-desc="{}"]/android.widget.RelativeLayout/android.widget.TextView[1]'
    call = 'com.android.contacts:id/dialButton'
    mute = '//android.widget.ImageButton[@content-desc="Mute"]'
    callEnd = '//android.widget.ImageButton[@content-desc="End"]'


class MessengerApp:
    search = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup"
    search2 = "android.widget.EditText"
    selectUser = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup"

    ChosePhoto = '//android.widget.ImageView[@content-desc="Choose photo"]'
    camera = '//android.widget.ImageView[@content-desc="Take photo"]'

    cameraPerform = '//android.widget.FrameLayout[@content-desc="Empty"]/android.widget.FrameLayout'
    cameraSend = '//android.widget.Button[@content-desc="Send"]/android.widget.ImageView'

    FrameLayoutText = 'android.widget.TextView'

    groupSearch = '/android.view.ViewGroup[@content-desc="2"]'


class HuaweiCamera:
    performPhoto = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]'
    performRecording = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]'
    photo_start = '//android.widget.TextView[@content-desc="This is Photo mode."]]'
    photo = '//android.widget.TextView[@content-desc="This is Photo mode."]'
    proMode = '//android.widget.TextView[@content-desc="This is Pro mode."]'
    video = '//android.widget.TextView[@content-desc="This is Video mode."]'
    portrait = '//android.widget.TextView[@content-desc="This is Portrait mode."]'





