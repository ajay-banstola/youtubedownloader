import youtube_dl
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class DownloadLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a text input field
        self.text_input = TextInput(hint_text="Paste YouTube link here")
        self.add_widget(self.text_input)

        # Create a download button
        self.download_button = Button(text="Download")
        self.download_button.bind(on_release=self.download_video)
        self.add_widget(self.download_button)

    def download_video(self, *args):
        # Get the YouTube link from the text input field
        youtube_link = self.text_input.text

        # Download the video using youtube-dl
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_link])


class DownloadApp(App):
    def build(self):
        return DownloadLayout()


if __name__ == '__main__':
    DownloadApp().run()

