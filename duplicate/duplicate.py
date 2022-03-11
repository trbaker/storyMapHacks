from arcgis import GIS
from arcgis.apps.storymap import StoryMap
gis = GIS("https://<your_org>.maps.arcgis.com","<username>","<password>")

# add as many quote usernames in your organization as needed.
users=["<username>"]

# end the storymap id that you wish to duplicate - two lines down
for user in users:
    story = StoryMap("<storymap_id>")
    temp=story.duplicate()
    print('Storymap Id duplicated: ' + temp.id )
    temp.reassign_to(user)

print("eof")
