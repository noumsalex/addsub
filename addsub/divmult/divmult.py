def mult(n1, n2):
  return n1 * n2


def div(n1, n2):
  try:
    return n1 / n2
  except Exception as e:
    raise Exception("An error occurred").with_traceback(traceback.exc_info()[2])
