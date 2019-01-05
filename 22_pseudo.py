N=3
ans = []
len(s) = 0, 

left=0, right=0,left<N, backtrack(s+'(',1,0),s='('
	left=1,right=0,left<N,backtrack(s+'(',2,0),s='(('
		left=2,right=0,left<N,backtrack(s+'(',2,0),s='((('
			left=3,right=0,right<left,backtrack(s+')',3,1),s='((()'
				left=3,right=1,right<left,backtrack(s+')',3,2),s='((())'
					left=3,right=2,right<left,backtrack(s+')',3,3),s='((()))'
						left=3,right=3,len(s)=6,ans=['((()))'],return
					return None
				return None
			return None
		left=2,right=0,right<left,backtrack(s+')',2,1),s='(()'
			left=2,right=1,left<N,backtrack(s+'(',3,1),s='(()('
				left=3,right=1,right<left,backtrack(s+')',3,2),s='(()()'
					left=3,right=2,right<left,backtrack(s+')',3,3),s='(()())'
						left=3,right=3,len(s)=6,ans=['((()))','(()())'],return
					return None
				return None
			left=2,right=1,right<left,backtrack(s+')',2,2),s='(())'
				left=2,right=2,left<N,backtrack(s+'(',3,2),s='(())('
					left=3,right=2,right<left,backtrack(s+')',3,3),s='(())()'
						left=3,right=3,len(s)=6,ans=['((()))','(()())','(())()'],return
					return None
				return None
			return None
		return None
	left=1,right=0,right<left,backtrack(s+')',1,1),s='()'
		left=1,right=1,left<N,backtrack(s+'(',2,1),s='()('
			left=2,right=1,left<N,backtrack(s+'(',3,1),s='()(('
				left=3,right=1,right<left,backtrack(s+')',3,2),s='()(()'
					left=3,right=2,right<left,backtrack(s+')',3,3),s='()(())'
						left=3,right=3,len(s)=6,ans=['((()))','(()())','(())()','()(())'],return
					return None
				return None
			left=2,right=1,right<left,backtrack(s+')',2,2),s='()()'
				left=2,right=2,left<N,backtrack(s+'(',3,2),s='()()('
					left=3,right=2,right<left,backtrack(s+')',3,3),s='()()()'
						left=3,right=3,len(s)=6,ans=['((()))','(()())','(())()','()(())','()()()'],return
					return None
				return None
			return None
		return None
	return None
return None


ans=['((()))','(()())','(())()','()(())','()()()']
				

