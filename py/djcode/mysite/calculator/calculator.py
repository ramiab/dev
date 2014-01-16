__author__ = 'rami'


def get_next_element_str(expression):
    if expression[0] in ['-', '+', '*', '/', '(']:
        elem = expression[0]
        return elem, expression[1:]

    ret_elem = ''
    while expression and expression[0].isdigit():
        ret_elem += expression[0]
        expression = expression[1:]
    return ret_elem, expression


def get_brackets_expression(cur_expression):
    """input example: (5+6dsjkhskdf(sfsfssf))"""
    stack = [0]
    for i in xrange(1, len(cur_expression)-1):
        if cur_expression[i] == '(':
            stack.append(i)
        elif cur_expression[i] == ')':
            stack.pop()

        if len(stack) == 0:
            return cur_expression[1:i]
    return cur_expression

def calc(expression):
    if type(expression) is not str:
        raise ValueError("expecting a string")

    queue = []

    cur_expression = expression
    while cur_expression:
        elem_str, cur_expression = get_next_element_str(cur_expression)
        print "elem_str = %s ; cur_expression = %s" % (elem_str, cur_expression)
        try:
            operand = int(elem_str)
            queue.append(operand)
        except ValueError:
            # operand2, cur_expression = get_next_element_str(cur_expression)
            operator = elem_str
            # operator, cur_expression = get_next_element_str(cur_expression)
            # print "operator = %s ; operand = %s ; cur_expression = %s" % (operator, operand, cur_expression)
            if operator=='(':
                brackets_expression = get_brackets_expression('('+cur_expression)
                tmp_operand = calc(brackets_expression)
                queue.append(tmp_operand)
                cur_expression = cur_expression.replace(brackets_expression+')', '')
            elif operator=='+' or operator=='-':
                queue.append(operator)
            elif operator == '*' or operator == '/':
                operand1 = queue.pop()
                operand2, cur_expression = get_next_element_str(cur_expression)
                operand2 = float(operand2)
                print "%s %s %s" % (operand1, operator, operand2)
                if elem_str=='*':
                    res_tmp = operand1*operand2
                else: # elem_str=='/':
                    res_tmp = operand1/operand2
                queue.append(res_tmp)
            else:
                raise ValueError('Unexpected element: %s'%elem_str)
        print "queue = %s" %queue

    total = queue.pop(0)
    while queue:
        operator = queue.pop(0)
        if type(operator) != str:
            raise ValueError('Unexpected element: %s; expecting and operator'%operator)

        operand = queue.pop(0)
        if not isinstance(operand, (int, long, float, complex)):
            raise ValueError('Unexpected element: %s; expecting and operand'%operand)
        if operator == '+':
            total += operand
        elif operator == '-':
            total -= operand
        else:
            raise ValueError('Unexpected element: %s; expecting and operator, + or -'%operator)
    return total
