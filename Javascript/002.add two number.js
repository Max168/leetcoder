/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var result = new ListNobe(0);
    var current = result;
    var carry = 0;
    while (l1 || l2){
        if (l1){
            var q = l1.val;
            l1 = l1.next;
        }else {
            q =0;
        }
        if (l2){
            var p = l2.val;
            l2 = l2.next
        }else {
            p = 0
        }
        var res = carry + q + p;
        if(res > 9){
            carry = 1;
            res = res % 10;
        }else {
            carry = 0;
        }
        current.next = new ListNobe(res);
        current = current.next;
    }
    if (carry == 1){
        current.next = new ListNobe(1);
    }
    return result.next;
};
