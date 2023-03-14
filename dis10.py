# Your name: 
# Your student id:
# Your email:
# List who you have worked with on this project:

## STEP 1: import necessary packages
import unittest


## STEP 2: Make your request

def get_xml():
    '''
    parameters: none
    returns: XML data

    grabs XML from https://www.w3schools.com/xml/plant_catalog.xml and passes back an XML object (not just a string)
    '''

    pass

## STEP 3: Answer question 1, What’s the price of a California poppy plant?

def poppy_price(xml_data):
    '''
    parameters: xml_data, xml object
    returns: the price of a poppy, int

    parses the XML data to find the price of a poppy
    '''

    pass

## STEP 3: Answer question 2, What plants from this list can I grow in zone 5? 

def zone5(xml_data):
    '''
    parameters: xml_data, xml object
    returns: list of plant names (each a string) that can be grown in zone 5

    parses the XML data to find which plants can be grown in zone 5

    Note: take a look at the xml file -- some of the 'zone' fields are formatted differently! They aren't all just a single digit
    '''

    pass

class plants_test(unittest.TestCase):
    def setUp(self):
        self.xml_data = get_xml()
        self.poppy = poppy_price(self.xml_data)
        self.zone5_list = zone5(self.xml_data)

    def test_poppy_price(self):
        self.assertEqual(self.poppy, '$7.89')

    def test_zone5(self):
        self.assertEqual(self.zone5_list, ['Trillium', 'Wake Robin', 'Primrose'])
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
