import jinja2
import os
import sys

djangobox_dir = os.path.join(os.path.dirname(
  os.path.abspath(__file__)), "..")

def create_template(in_file, out_file, var_dic):
    """
    >>> create_template('scripts/jtest.txt', 'scripts/out.txt', 
      {'name':'Pete'})
    None
    """
    in_template_path = os.path.join(djangobox_dir, in_file)
    with open(in_template_path, "r") as in_fi:
        inp = in_fi.read()
    template = jinja2.Template(inp)
    rendered_template = template.render(var_dic)
    out_template_path = os.path.join(djangobox_dir, out_file)
    with open(out_template_path, "w") as out_fi:
        out = out_fi.write(rendered_template)
    #print rendered_template

