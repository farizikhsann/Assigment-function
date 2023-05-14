# ENKRIPSI
if __name__ == '__main__':

  def enkripsi(text):
      hasil= ''
      text = text.upper()
      for i in range(len(text)):
          if(text[i].isalpha()):
              if(ord(text[i]) > 86):
                  hasil += chr(91-ord(text[i])+65)
              else:
                  hasil += chr(ord(text[i])+4)
          else:
              hasil += text[i]
      return hasil

  print(enkripsi("Meet me by the rose bushes tonight."))
