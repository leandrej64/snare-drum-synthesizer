from concurrent.futures import ThreadPoolExecutor, as_completed


class Generator :
    def __init__(self,instrument,parameters,store_audio=True,store_npz=False,max_workers=10): 
        self.instrument = instrument 
        self.max_workers= max_workers
        self.parameters = parameters
    def generate_one(self,parameter):
        instrument = self.instrument(*parameter['list'])
        instrument.store_audio(f"samples/{parameter['name']}.wav")
        print(f"Generated parameters {parameter['name']}")

    
    def generate(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as pool :
            futures = [pool.submit(self.generate_one,parameter) for parameter in self.parameters]
            for fut in futures  :
                fut.result()

                
