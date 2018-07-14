from dmock import DataMocker

d = DataMocker()

# We want to be able to reproduce the same output given the same seed.
d.seed(110)

# This should change the way the data are formatted and not the data itself.
d.context.locale("en_US")

# Return an Address object with all fields populated.
d.address.create()

# Returns strings.
d.address.street()
d.address.city()

# Returns strings.
d.person.name()
d.person.surname()
# Return an Address object provided from dmock itself.
d.person.address()

# Change the way the data are produced, from now on all people will have italian names.
d.person.context.country("it")
# This will produce an italian address.
d.person.address()
# This will return a date but because of the locale this will be formatted using US settings.
d.person.birthdate()

d.person.context.country("it")
# Default country, if nothing is set this will be used
d.context.country("us")
# All addresses produced from the address provided will be from the uk
d.address.context.country("uk")
# This will be a UK address where lives an italian person
# Another alternative is to produce an italian address, because person's context is set to it.
d.person.address.create()

# This should raise an exception or not? If is not a problem then this provider should continue to produce data with the previous setting.
d.person.context.country("invalid")

# Should this address be from italy, usa or uk?
d.person.address.create()

d.person.context.age(lambda age: age > 23)
