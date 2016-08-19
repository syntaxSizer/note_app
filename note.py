#/usr/bin/python
class NotesApplication (object):
  note_content = raw_input('any notes for today ?')

  not_id = 0
  def __init__(self,author,my_saved_notes, not_id):
    NotApplication.not_id +=1
    self.author=author
    self.my_saved_notes = []
    self.id= note_id

  def create(self, note_content):
    self.my_saved_notes.append(note_content)
    

  def list(self):
      print("note id: " self.id)
      print(self.my_saved_notes)
      print("by Author :" self.author)
  
  #return the note 
  def get (self,note_id):
      return str(my_saved_notes[note_id])
  
# search 
  def search (self, search_text):
    for note in my_saved_notes):
        for text in note:
          if search_text == text:
            print 'result for search'
            self.list()
            print '/n'


  def delete(self,note_id):
    self.my_saved_notes.pop(note_id)

  
  def edit(self,note_id,new_content):
    new_content = raw_input('new content ')
    my_saved_notes[note_id] = new_content
    self.list()
    print '/n'  





          



               

          




      