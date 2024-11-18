from model import model_train, model_load
import sys, os

def main():
    
    ## train the model
    data_dir = os.path.join("data","cs-train")
    model_train(data_dir,test=True)

    ## load the model
    all_data, all_models = model_load()
    
    print("model training complete.")


if __name__ == "__main__":

    main()
