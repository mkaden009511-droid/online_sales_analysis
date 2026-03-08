# Online Sales Analysis

## Opis projekta
Ovaj projekat omogućava praćenje proizvoda i upravljanje prodajom koristeći Python klase i Git verzionisanje.

## Klase

### Product
- Atributi: `name`, `price`, `quantity`
- Metodi:
  - `show_info()`: prikazuje informacije o proizvodu
  - `update_quantity(new_quantity)`: ažurira količinu proizvoda

### ProductManager
- Atributi: lista svih proizvoda
- Metodi:
  - `add_product(product)`: dodaje proizvod u listu
  - `show_products()`: prikazuje sve proizvode
  - `total_value()`: prikazuje ukupnu vrednost inventara
  - `remove_product(name)`: uklanja proizvod po imenu

### Cart
- Atributi: `cart_items` (lista proizvoda u korpi)
- Metodi:
  - `add_to_cart(product)`: dodaje proizvod u korpu
  - `show_cart()`: prikazuje sadržaj korpe
  - `total_amount()`: prikazuje ukupnu vrednost za naplatu

## Korišćenje
1. Pokrenuti `main.py`  
2. Dodavati proizvode u `ProductManager`  
3. Dodavati proizvode u `Cart` i prikazivati sadržaj i ukupnu vrednost

## Git funkcionalnosti
- Projekat koristi grane za dodavanje novih funkcionalnosti (`add-product-removal`, `add-cart-functionality`)  
- `.gitignore` je podešen da ignoriše `config.json` i slike