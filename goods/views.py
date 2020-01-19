from goods import goods_blue
from flask import jsonify

@goods_blue.route('/g1')
def g():
    return jsonify({'name':'goods1'})

@goods_blue.route('/g2',methods=['post'])
def g2():
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - users
    parameters:
      - in: path
        name: username
        type: string
        required: true
    responses:
      200:
        description: A single user item
        schema:
          id: rec_username
          properties:
            username:
              type: string
              description: The name of the user
              default: 'steve-harris'
    """
    return jsonify({'name':'goods2'})