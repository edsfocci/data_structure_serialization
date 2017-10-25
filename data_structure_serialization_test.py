import unittest
from data_structure_serialization import serialize

class TestDataStructureSerialization(unittest.TestCase):

  def test_serialize_int_to_html(self):
    self.assertEqual(serialize(1, 'html'), '1')

  def test_serialize_float_to_html(self):
    self.assertEqual(serialize(1.0, 'html'), '1.0')

  def test_serialize_str_to_html(self):
    self.assertEqual(serialize('1.00', 'html'), '1.00')

  def test_serialize_empty_list_to_html(self):
    self.assertEqual(serialize([], 'html'), '<ol></ol>')

  def test_serialize_empty_dict_to_html(self):
    self.assertEqual(serialize({}, 'html'), '<dl></dl>')

  def test_serialize_nested_lists_dicts_to_html(self):
    self.assertEqual(serialize(
      [
        'a',
        {
          'b': 'c',
          'd': 'e',
          'f':
          [
            'g',
            'h'
          ]
        },
        'i'
      ]
      , 'html'),
      '<ol>' +
        '<li>' +
          'a' +
        '</li>' +
        '<li>' +
          '<dl>' +
            '<dt>' +
              'f' +
            '</dt>' +
            '<dd>' +
              '<ol>' +
                '<li>' +
                  'g' +
                '</li>' +
                '<li>' +
                  'h' +
                '</li>' +
              '</ol>' +
            '</dd>' +
            '<dt>' +
              'd' +
            '</dt>' +
            '<dd>' +
              'e' +
            '</dd>' +
            '<dt>' +
              'b' +
            '</dt>' +
            '<dd>' +
              'c' +
            '</dd>' +
          '</dl>' +
        '</li>' +
        '<li>' +
          'i' +
        '</li>' +
      '</ol>')

  def test_serialize_nested_dicts_lists_to_html(self):
    self.assertEqual(serialize(
      {
        'z':
        [
          'y',
          {
           'x': 'w',
           'v': 'u'
          }
        ],
        't': 's'
      }
      , 'html'),
      '<dl>' +
        '<dt>' +
          'z' +
        '</dt>' +
        '<dd>' +
          '<ol>' +
            '<li>' +
              'y' +
            '</li>' +
            '<li>' +
              '<dt>' +
                '<dt>' +
                  'x' +
                '</dt>' +
                '<dd>' +
                  'w' +
                '</dd>' +
                '<dt>' +
                  'v' +
                '</dt>' +
                '<dd>' +
                  'u' +
                '</dd>' +
              '</dt>' +
            '</li>' +
          '</ol>' +
        '</dd>' +
        '<dt>' +
          't' +
        '</dt>' +
        '<dd>' +
          's' +
        '</dd>' +
      '</dl>')


if __name__ == '__main__':
  unittest.main()
