function assert(condition, message) {
    if (!condition) {
        throw message || "Assertion failed";
    }
}

var d = {'Yoni':0.1, 'Benny':0.2, 'Moshe':0.4, 'Orian':0.3};

function getNameByProbability1(){
    var rand = Math.floor((Math.random()*10)+1);
    //console.debug('rand = '+rand);
    var i = 0;
    for(key in d){
        //console.debug(key+'-->'+d[key]);
        var j = d[key]*10;
        if(i+j >= rand){
            return key;
        }
        i += j;
    }
}
console.debug('New Name 1 = '+getNameByProbability1());

//---------
function NamesGenerator(prob_dict){
    var prob_dict = prob_dict;
    var names_arr = [];
    var prepareProbabilities = function(){
        var cur = 0;
        var total_p = 0;
        for(key in prob_dict){
            console.debug(key+'-->'+prob_dict[key]);
            var p = prob_dict[key]*10;
            total_p += p
            console.debug('p='+p);
            for( var i=0; i<p; i++ ){
                names_arr.push(key);
            }
        }
        assert(total_p == 10);
    };
    prepareProbabilities();
    this.getNameByProbability2 = function(){
        var rand = Math.floor(Math.random()*10);
        //console.debug('rand = '+rand);
        return names_arr[rand];
    }
}

var names_gen = new NamesGenerator(d);
console.debug('New Name 2 = '+names_gen.getNameByProbability2());



//---------
function test(test_title, gen_func){
    console.debug('---------------');
    console.debug(test_title);
    test_d = {};
    var test_num = 10000;
    for(i=0; i<test_num; i++){
        var name = gen_func();
        if(test_d[name]){
            test_d[name] = test_d[name]+1;
        }
        else {
            test_d[name] = 1;
        }
    }

    for(item in test_d){
        test_d[item] = test_d[item]/test_num;
    }
    console.debug('test_d = '+JSON.stringify(test_d));
    var total_prob = 0;
    for(item in test_d){
        total_prob += test_d[item];
    }
    console.debug('total_prob = '+total_prob);
    console.debug('---------------');
}

test('getNameByProbability1', getNameByProbability1);
test('names_gen.getNameByProbability2', names_gen.getNameByProbability2);
