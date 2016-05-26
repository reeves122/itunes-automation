import sys
sys.path.append('pyitunes/')
from pyItunes import *
import csv
from pyItunes.XMLLibraryParser import XMLLibraryParser
import argparse


# Description:
#  This script will scan your iTunes library XML file (using pytunes) and export every item to a CSV file,
#
# Usage:
#  Run the script supplying the required arguments.
#
# Example:
#  python export_csv.py --xmlfile="iTunes Music Library.xml" --outputfile="itunes_library.csv"

parser = argparse.ArgumentParser(description='Creates a CSV of the items in your iTunes library')
parser.add_argument('--xmlfile', help='Input iTunes Music Library.xml')
parser.add_argument('--outputfile', help='Output CSV file')
args = vars(parser.parse_args())

library = Library(args['xmlfile'])

f = open(args['outputfile'], 'wt')

# Write header row
writer = csv.writer(f, delimiter=',')
writer.writerow(('Artist', 'Album', 'Name', 'Track Number', 'Genre', 'Rating', 'Play Count'))

for song in library.songs.items():
     if song[1].artist != '':
         if  song[1].album != '':
             try: artist = (song[1].artist).encode('utf-8')
             except: artist = ''

             try: album = (song[1].album).encode('utf-8')
             except: album = ''

             try: name = (song[1].name).encode('utf-8')
             except: name = ''

             try: track_number = song[1].track_number
             except: track_number = ''

             try: genre = song[1].genre
             except: genre = ''

             try: rating =song[1].rating
             except: rating = ''

             try: play_count = song[1].play_count
             except: play_count = ''

             writer.writerow((artist, album, name, track_number, genre, rating, play_count))

print
