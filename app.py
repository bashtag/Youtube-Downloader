from gui.gui import Gui
import gui.constants as cnst
from pytube import YouTube as YT
from pytube import Playlist as PL
		
class App(Gui):
	def __init__(self):
		super().__init__(cnst.APP_NAME, "550", "250")

	def download(self, url):
		if "watch" in url:
			try:
				video = YT(url)
			except:
				print("URL ERROR")
				return None
			print(f"{video.title} is downloading")
			
			type_res = self.res_val.get()
			if type_res == "mp3":
				print("mp3 downloader")
				return None
		
			res = cnst.OPMENU_LIST[1:]
			for resolution in res[res.index(type_res):]:
				down_video = video.streams.get_by_resolution(resolution)
				if down_video == None:
					continue
				else:
					down_video.download()
		else:
			print("getting playlist...")
			print(self.entry.get())
			try:
				playlist = PL(self.entry.get())
			except:
				print("Playlist URL ERROR")
				return None
			print(f"{playlist.title} is downloading")
			print(type(self.first.get()),type(self.second.get()))
			print(int(self.first.get()), int(self.second.get()))

			type_res = self.res_val.get()
			if type_res == "mp3":
				print("mp3 downloader")
				return None

			for video in playlist.video_urls[int(self.first.get())+1:int(self.second.get())+1]:
				self.download(video)

	def exec(self):
		self.entry = super().url_frame()
		self.res_val = super().res_frame()
		(self.first, self.second) = super().pl_number_frame()
		super().down_button(self.download)
		super().loop()