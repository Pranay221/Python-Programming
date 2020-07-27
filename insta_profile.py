import qrcode

my_profile = "https://www.instagram.com/i.m.pranayy/"
filename = "my_instaprofile.png"
imgx = qrcode.make(my_profile)
imgx.save(filename)
