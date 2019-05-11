from music21 import converter, chord

class MusicParser:
  def __init__(self, filename):
    self.filename = filename

  def parse(self):
    music = converter.parse(self.filename)
    music = music.chordify()
    
    chords = music.flat.getElementsByClass(chord.Chord)
    
    return list(chords), [len(c.pitches) for c in chords]
