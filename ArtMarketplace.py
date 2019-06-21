class Listing:
  
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
    
  def __repr__(self):
    return "%s. %s." %(self.art.title, self.price)
  

class Clients:
  def __init__(self, name, location, is_museum, money, wishlist):
    
    self.name = name
    self.location = location
    self.is_museum = is_museum
    self.money = money
    self.wishlist = wishlist
    
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
      self.money += new_listing.price
      
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
        self.money -= art_listing.price
        
  def wallet(self):
    print("%s's balance equals %s dollars."%(self.name, str(self.money)))
    
# Clients
edytta = Clients("Edytta Halpirt", "Private Collection", False, 6000000, [])
moma = Clients("The MOMA", "New York", True, 12000000, [])


class Marketplace:

  
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
        
  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)
          
  def show_listings(self):
    for item in self.listings:
      print(item)

veneer = Marketplace()

class Art:
  
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return '%s. "%s". %s, %s. %s, %s.' %(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location) 

  
# Works of Art
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
sunflowers = Art("van Gogh, Vincent", "Sunflowers", "oil on canvas", 1887, moma)
stormysea = Art("van Rijn, Rembrandt", "Storm at Sea", "poop on pants", 1633, edytta)

# Commands
edytta.sell_artwork(girl_with_mandolin, 6000000)
moma.buy_artwork(girl_with_mandolin)
veneer.show_listings()


print(girl_with_mandolin)
print(moma.money)
print(edytta.money)
Clients.wallet(edytta)
veneer.add_listing(sunflowers)
veneer.add_listing(stormysea)
veneer.show_listings()
edytta.wishlist.append(sunflowers)
print(edytta.wishlist)
