import sys
import time
import xmltodict
import magicdate
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

#from .models import Media


class MyHandler(PatternMatchingEventHandler):
    patterns=["*.xml"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """

        with open(event.src_path, 'r') as xml_source:
            xml_string = xml_source.read()
            parsed = xmltodict.parse(xml_string)
            print parsed

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()