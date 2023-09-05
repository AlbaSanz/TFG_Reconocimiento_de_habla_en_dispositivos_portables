import os
from typing import Union

import datasets
import pandas as pd

_DESCRIPTION = "" 
_HOMEPAGE = ""

DATA_DIR = {"train": "AudioWAV"}
ARCHIVO_CSV = 'csvravdess.csv'
CSV_DIR = os.path.dirname(os.path.abspath(ARCHIVO_CSV))
ARCHIVO = os.path.join(CSV_DIR, ARCHIVO_CSV)
data_frame = pd.read_csv(ARCHIVO)

class NewDataset(datasets.GeneratorBasedBuilder):
  
  DEFAULT_WRITER_BATCH_SIZE = 256
  BUILDER_CONFIGS = [datasets.BuilderConfig(name="clean", description="Train Set.")]

  def _info(self):
    #information about dataset
    return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {"file": datasets.Value("string"), "label": datasets.Value("string")}
            ),
            supervised_keys=("file", "label"),
            homepage=_HOMEPAGE,
        )
  
  def _split_generators(
        self, dl_manager: datasets.utils.download_manager.DownloadManager
    ):
        data_dir = dl_manager.extract(self.config.data_dir)
        if self.config.name == "clean":
            train_splits = [
                datasets.SplitGenerator(
                    name="train", gen_kwargs={"files": data_dir, "name": "train"}
                )
            ]

        return train_splits
  
  def _generate_examples(self, files: Union[str, os.PathLike], name: str):
        """Generate examples from a Crema unzipped directory."""
        key = 0
        examples = list()

        audio_dir = os.path.join(files, DATA_DIR[name])
        csv_dir = os.path.join(files, CSV_DIR)

        if not os.path.exists(audio_dir):
            raise FileNotFoundError
        else:
            for file in os.listdir(audio_dir):
                resultado = data_frame[data_frame['filename'] == file]['annotated_discrete_emotion']
                emocion = str(resultado).split('\n')[0]
                emocion = emocion.split(' ')[-1]

                if emocion != 'NaN':
                    res = dict()
                    res["file"] = "{}".format(os.path.join(audio_dir, file))
                    res["label"] = emocion
                    examples.append(res)
                else:
                    print('No tiene emocion asociada')

        for example in examples:
            yield key, {**example}
            key += 1
        examples = []