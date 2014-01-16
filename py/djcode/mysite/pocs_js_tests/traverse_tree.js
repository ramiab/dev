function Node(name){
    var name = name;
    var children = [];
    this.addChild = function(node){
        children.push(node);
    }
    this.getName = function(){
        return name;
    }
    this.getChildren = function(){
        return children;
    }
    this.printRecursively = function(prefix){
        console.log(prefix+'-- '+name);
        for(var i=0; i<children.length; i++){
            children[i].printRecursively('  '+prefix);
        }
    }
}

function NodeIterativeWalker(root){
    var queue = [root];
    root.level = 0;
    this.printNode = function(node){
       var prefix = Array(node.level).join(" ");
       console.debug(prefix+'-- '+node.getName());
    }
    this.printIterativeUsingQueue = function(){
        while( queue.length > 0 ) {
            var node = queue.shift();
            this.printNode(node);
            var children = node.getChildren();
            for( var i=0 ; i<children.length; i++ ){
                children[i].level = node.level + 1 ;
                queue.push(children[i]);
            }
        }
    }

    var stack = [root];
    this.printIterativeUsingStack = function(){
        while( stack.length > 0 ) {
            var node = stack.pop();
            this.printNode(node);
            var children = node.getChildren();
            for( var i=children.length-1 ; i>=0; i-- ){
                children[i].level = node.level + 1 ;
                stack.push(children[i]);
            }
        }
    }
}

var root = new Node('root');
var n1 = new Node('n1');
var n2 = new Node('n2');
var n11 = new Node('n11');

root.addChild(n1);
root.addChild(n2);
n1.addChild(n11);

root.printRecursively('');

console.debug('---------------');
var nodeWalker = new NodeIterativeWalker(root);
nodeWalker.printIterativeUsingQueue();

console.debug('---------------');
nodeWalker.printIterativeUsingStack();