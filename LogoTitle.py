from Extra import *

class LogoTitle(Extra):

	__sr = re.compile(".*logo.*", re.IGNORECASE)
	
	def __par_a(self, s):
		a = (s.name=='img') and (s.parent.name=='a')
	
		if a is True:
			t=s.parent
			url = t['href']
			b = up.urlparse(url)
			c = up.urlparse(self.home_page)
		
			if b[1] == c[1]:
				return True
			else:
				return False
		
		return False
		


	def __iall(self):
		for a in self.find_all('img'):
			for b in a.attrs:
				
				if isinstance(a[b], list):       # when the attribute takes multiple values
					a[b] = ' '.join(a[b])
				
				if bool(re.match(self.__sr, a[b])):   # str(a[b]) -> attr vlue may be in a list
					return a
		
		return None



	def get_logo(self):
		
		t = self.find('img', attrs={'src': LogoTitle.__sr})  # first image with 'logo' keyword
		
		if t is None:                # link to home page heuristic
			t = self.find(self.__par_a)
	
		#if t is None:        # searching all images for 'logo' keyword
		#	t = self.__iall()
		
		#if t is None:                   # first image heuristic -> very dangerous
		#	t = self.find('img')
		
	
		
		if t is not None:
			print("logo found->", end="")
			self.download_image(t['src'])
		else:
			print("No logo Found ->", self.home_page)
	
	
	def download_image(self, src):
		
		a = list(up.urlparse(src))
		b = list(up.urlparse(self.home_page))
		
		a[0]=b[0]
		
		if a[1]=='':	
			a[1]=b[1]
			
		a=up.urlunparse(a)
		
		ur.urlretrieve(a, "logo")
		print("downloaded")
		
		
	
	def get_title(self):
		s = self.head.find('title').string
		
		print("title found->saved")
		
		with open("title", "w") as fi:
			fi.write(s)
			
		
	

url = 'http://nielit.gov.in/patna/'
print(url)



     #Loading a page takes most of the time

soup=LogoTitle(load_page(url), 'lxml')

soup.home_page=url
soup.cur_page=url
soup.urls.append(url)

print(soup.home_page, soup.cur_page, soup.urls, soup.tsites)

soup.get_logo()
soup.get_title()