import instaloader
from instaloader import  Profile
import os
ig = instaloader.Instaloader()

#*420madisonivy, iryna_playmate, yvonne_bar_backup, playboyiryna, irynanova_, c_dvre, misscjmiles, 
#* annelesemilton, therealellematthews, jessicafitcake, ashtens_empire, razor_candi, playmatekikii,
#* mym_official_ig, lynaritaa, romirain, connyhawk, misscjmiles_s

#*Definir ruta donde se cargan las fotos
os.chdir('D:/OneDrive - Universidad de los Andes/Photos/NN_Deep')
req_user = input("user name of profile you want to download ")
#* 1.downloading profile pictures
#ig.download_profile(req_user, profile_pic=True)
#* 2 downloading profile posts
#* for public
ig.download_profile(req_user)
#* for private
#username = input("your user name ")
#password = input("your password ")
#ig.login(username, password)
#ig.download_profile(req_user)

#* 3 downloaing tagged posts
#* for public
#profile = instaloader.Profile.from_username(ig.context, req_user)
#ig.download_tagged(profile.username)
#* for private
#req_user = input("user name of profile you want to download ")
#username = input("your user name ")
#password = input("your password ")
#profile = instaloader.Profile.from_username(ig.context, req_user)
#ig.download_tagged(profile.username)

#* 4 downloading stories
#ig.download_profile(req_user, download_stories=True)
#* or
#profile = ig.check_profile_id(req_user)
#profile_id = profile.userid
#print(profile_id)
#ig.download_stories([profile_id])
#* downloading profile stories and tagged posts
#ig.download_profile(req_user, profile_pic=True, download_stories=True, download_tagged=True)

#* 5 downloading igtv videos
#profile = Profile.from_username(ig.context, req_user)
#ig.download_igtv(profile)

#* 6 downloading hashtag posts
#HASHTAG=input("enter hash tag name ")
#for post in ig.get_hashtag_posts(HASHTAG):
#    ig.download_post(post, target='#'+HASHTAG)