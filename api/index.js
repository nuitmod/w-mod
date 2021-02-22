var exp_data= {
      "mod1": {
        "name1": "Ruth",
        "job1": "programmer"
      },
      "mod2": {
        "name2": "Miut",
        "job2": "contacter"
      }
    }

var item_data={
  "items":[
{
        "name": "Ruth",
        "job": "programmer"
      },
      {
        "name": "Miut",
        "job": "contacter"
      }

]
}

module.exports=(req,res)=>{
  res.json(item_data);
}
