!pip install -q pyannote.audio==1.1


# Import statements: put these at the top of you files
import torch
import google.colab
import csv
from pyannote.database.util import load_rttm
from pyannote.core import Segment, notebook
from pyannote.audio.features import RawAudio
from IPython.display import Audio

# Load dia type pyannote-audio pipeline via pytorch
model_type = 'pyannote/pyannote-audio'
pipeline_type = 'dia'
pipeline = torch.hub.load(model_type, pipeline_type)

# Input file stuff specific to google colabs
own_file, _ = google.colab.files.upload().popitem()

input_file_dict = {
    'audio': own_file
    }

# load audio waveform and play it
waveform = RawAudio(sample_rate=44100)(OWN_FILE).data
Audio(data=waveform.squeeze(), rate=44100, autoplay=True)

# Get annotation from pipeline
annotation = pipeline(input_file_dict)

overlap_detection = torch.hub.load('pyannote/pyannote-audio', 'ovl_ami', pipeline=True)
overlap_detection(own_file).get_timeline()

# We Write the annotation to file
output_file_path = 'file.rttm'
with open(output_file_path, 'w') as file:
    annotation.write_rttm(file)

# Load annotation again - im not sure what the load_rttm method returns.
# will have to check
loaded_object = load_rttm(output_file_path)


annotation.chart()

# find speaker with largest duration
print '%f spoke for %f seconds' % annotation.argmax(), annotation.label_duration(annotation.argmax())

#annotation.argmax()

#not sure if this is doing the same as above .. it's a different structure but I Think it's the same data...?
data = []
segments = []
tracks = []
labels = []
annotation_data = {}
for segment, track, label in annotation.itertracks(yield_label=True):
    print("{} {} {}".format(segment, track, label))
    annotation_data[label] = ""
    segments.append(segment)
    tracks.append(track)
    labels.append(label)

for key, value in annotation_data.items():
    print("{} {}".format(key, value))
    print("{} {} {}".format(key, value.get('segment'), value.get('track')))

data=[(segment, track, label)]

with open('test_dia.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['segment', 'track', 'label'])
    for row in data:
        csv_out.writerow(row)