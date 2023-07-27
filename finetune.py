from autotrain import AutoTrain

# create an instance of AutoTrain
at = AutoTrain()

# specify the task, dataset, and output directory
task = "text_classification"
dataset = "path/to/your/dataset.csv"
output_dir = "path/to/your/output/directory"

# start a training job
at.train(task=task, dataset=dataset, output_dir=output_dir)
