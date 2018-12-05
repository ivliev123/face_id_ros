# face_id

## 
```bash
cd catkin_wc
git clone https://github.com/ivliev123/face_id_ros
```

### Установка нужных для работы модулей
```bash
sudo pip install scikit-image
sudo pip install imutils
sudo pip install opencv-python
sudopip install datetime
sudo apt-get install -y cmake

sudo pip install dlib
```
## Сборка под ROS(если сразу не заработало) 

```bash
cd face_id_ros/
cd skripts/
chmode 777 face_id.py
chmode 777 make_dictionary.py
```

## Запуск для создания словаря дескрипторов
rosrun make_dictionary

## Запуск распознавалки
rosrun face_id
