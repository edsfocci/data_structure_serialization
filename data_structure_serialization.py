import re

def serialize(data, serialization_type):

  def jsonify_str(text):
    result_text = re.compile(r'\\?\"').sub(r'\\"', text)
    result_text = re.compile(r"\\?'").sub(r"'", result_text)

    return '"{}"'.format(result_text)

  def serialize_to_json(data_chunk):
    output_text = ''
    type_of_data = type(data_chunk)

    if type_of_data in {int, float}:
      output_text = str(data_chunk)

    elif type_of_data is str:
      output_text = jsonify_str(data_chunk)

    elif type_of_data is list:
      temp_list = []
      output_text += '['
      for item in data_chunk:
        temp_list.append(serialize_html(item))
      output_text += ', '.join(temp_list)
      output_text += ']'

    elif type_of_data is dict:
      temp_list = []
      output_text += '{'
      for key, val in data_chunk.items():
        temp_list.append(
          jsonify_str(key) +
          ': ' +
          serialize_html(val)
        )
      output_text += ', '.join(temp_list)
      output_text += '}'

    return output_text

  def serialize_to_html(data_chunk):
    output_text = ''
    type_of_data = type(data_chunk)

    if type_of_data in {int, float, str}:
      output_text = str(data_chunk)

    elif type_of_data is list:
      output_text += '<ol>'
      for item in data_chunk:
        output_text += '<li>{}</li>'.format(serialize_to_html(item))
      output_text += '</ol>'

    elif type_of_data is dict:
      output_text += '<dl>'
      for key, val in data_chunk.items():
        output_text += '<dt>{}</dt>'.format(key)
        output_text += '<dd>{}</dd>'.format(serialize_to_html(val))
      output_text += '</dl>'

    return output_text


  serialized_output = ''

  if serialization_type.lower() == 'json':
    serialized_output = serialize_to_json(data)
  elif serialization_type.lower() == 'html':
    serialized_output = serialize_to_html(data)

  return serialized_output
