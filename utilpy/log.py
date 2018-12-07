"""Logger function that print time required in each session of logger"""

import time

class Logger(object):
    """
    Print the log message with time required between each session
    New session should start with "<" and end with ">"
    session ends with "</>"
    """

    def __init__(self):
        self._sections = []
        self._delimiter = '|'
        self._space = 3 * ' '


    def _write(self, message):
        print(len(self._sections) * (self._delimiter + self._space) + str(message))


    def _calculate_duration(self, start_epoch, end_epoch):

        duration = end_epoch - start_epoch
        minutes = int(duration // 60)
        seconds_digits = 0
        duration_string = ''

        if duration >= 60:
            duration_string += str(minutes) + ' min '
        elif duration >= 10:
            seconds_digits = 1
        elif duration >= 1:
            seconds_digits = 2
        else:
            seconds_digits = 3

        seconds = round(duration - 60*minutes, seconds_digits)
        if seconds_digits == 0:
            seconds = int(seconds)
        duration_string += str(seconds) + ' sec'
        return duration_string


    def _update_latest_event(self, val):
        if len(self._sections):
            self._sections[-1]['latest_event'] = val


    def _start_section(self, message):
        self._write('')
        self._write(message)
        new_section = {'start_time': time.time(), 'latest_event': 'start_section'}
        self._sections.append(new_section)


    def _add_line(self, message):
        if len(self._sections) and self._sections[-1]['latest_event'] in ('start_section', 'end_section'):
            self._write('')
        self._write(message)
        self._update_latest_event('add_line')


    def _end_section(self):
        if len(self._sections) == 0:
            raise SyntaxError("Please open a new log section before attempting to close one")
        start_time = self._sections[-1]['start_time']
        duration_string = self._calculate_duration(start_time, time.time())
        if self._sections[-1]['latest_event'] != 'start_section':
            self._write('')
        self._sections.pop()
        self._write('( ' + duration_string + ' )')
        self._update_latest_event('end_section')


    def log(self, message):
        """log message 
	   ``new session`` starts with ``<`` and ends with ``>``
           ``session end`` with ``</>``
        """

        if message == '</>':
            self._end_section()
        elif len(message) >= 2 and message[0] == '<' and message[-1] == '>':
            self._start_section(message[1:-1])
        else:
            self._add_line(message)

