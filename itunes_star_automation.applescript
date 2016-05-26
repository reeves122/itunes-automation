-- Description:
--  This script expects to find 5 playlists in your iTunes Library, each representing a star rating.
--  It will then set each track's rating equal to the playlist it is contained in. This is useful when you
--  regularly listen to music on a device that does not support star ratings but
--  you want to rate your tracks anyway (like Apple TV and Android).

tell application "iTunes"
	set tracks_1star to tracks of playlist "Automation 1 Stars"
	repeat with a_track in tracks_1star
		set rating of a_track to 20
	end repeat
	
	set tracks_2star to tracks of playlist "Automation 2 Stars"
	repeat with a_track in tracks_2star
		set rating of a_track to 40
	end repeat
	
	set tracks_3star to tracks of playlist "Automation 3 Stars"
	repeat with a_track in tracks_3star
		set rating of a_track to 60
	end repeat
	
	set tracks_4star to tracks of playlist "Automation 4 Stars"
	repeat with a_track in tracks_4star
		set rating of a_track to 80
	end repeat
	
	set tracks_5star to tracks of playlist "Automation 5 Stars"
	repeat with a_track in tracks_5star
		set rating of a_track to 100
	end repeat
end tell