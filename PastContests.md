## 過去問
|Q|Diff|Point|
|:----|:----|:----|
|[ABC041D](https://atcoder.jp/contests/abc041/tasks/abc041_d)||N=15~20のパターン数はまずbitDP|
|[ABC061D](https://atcoder.jp/contests/abc061/tasks/abc061_d)||経路の最大スコア(最長経路)は重みを負にしたベルマンフォード。頂点Nが負閉路の影響を受けるか判断するにはN回更新して頂点Nの変化の有無を見る|
|[ABC078D](https://atcoder.jp/contests/abc078/tasks/arc085_b)||N^2までいけるなら[メモ化ミニマックス](https://blog.hamayanhamayan.com/entry/2017/11/11/225532)かも|
|[ABC082D](https://atcoder.jp/contests/abc082/tasks/arc087_b)||爆発しそうな座標問題もx,y別々で処理可能なら間に合う|
|[ABC091D](https://atcoder.jp/contests/abc091/tasks/arc092_b)||XORは桁ごとに和の奇遇を計算。sumが絡むならmod2^(k+1)シーリングが有効かも|
|[ABC107D](https://atcoder.jp/contests/arc101/tasks/arc101_b)||中央値は二分探索＋[転倒数](https://qiita.com/wisteria0410ss/items/296e0daa9e967ca71ed6)でいけるかも|
|[ABC127E](https://atcoder.jp/contests/abc127/tasks/abc127_e)||その組み合わせが何回数えられるか＋マンハッタンは縦横分解可|
|[ABC130E](https://atcoder.jp/contests/abc130/tasks/abc130_e)||最長共通部分列(LCS)のDP＋二次元累積和|
|[ABC136E](https://atcoder.jp/contests/abc136/tasks/abc136_e)||約数でループ|
|[ABC137D](https://atcoder.jp/contests/abc137/tasks/abc137_d)||時限タスクの優先順は時間遡りが有効なことも|
|[ABC137E](https://atcoder.jp/contests/abc137/tasks/abc137_e)||最長経路は-1倍で最短経路問題＋負辺あるならベルマンフォード|
|[ABC139F](https://atcoder.jp/contests/abc139/tasks/abc139_f)||偏角ソート後に探索|
|[ABC141F](https://atcoder.jp/contests/abc141/tasks/abc141_f)||XORの最大値は掃き出し法|
|[ABC143E](https://atcoder.jp/contests/abc143/tasks/abc143_e)||N^3で許されるならワーシャルフロイド|
|[ABC144F](https://atcoder.jp/contests/abc144/tasks/abc144_f)||N到達までの行動回数期待値問題はゴール側から計算(到達可能領域の回数期待値の和/選択肢数 + 1回)|
|[ABC148E](https://atcoder.jp/contests/abc148/tasks/abc148_e)||末尾のゼロの個数はmin(因数2の個数,因数5の個数)|
|[ABC154F](https://atcoder.jp/contests/abc154/tasks/abc154_f)||二次元累積和|
|[ABC160F](https://atcoder.jp/contests/abc160/tasks/abc160_f)||木パターン列挙は木DP＋全方位木DP|
|[ABC164D](https://atcoder.jp/contests/abc164/tasks/abc164_d)||区間に関する問題において、累積和的なものを考える(158Eで既出)|
|[ABC167D](https://atcoder.jp/contests/abc167/tasks/abc167_d)||ループはダブリングでいける([解説](https://drken1215.hatenablog.com/entry/2020/06/20/190700))175D,241Eも|
|[ABC171F](https://atcoder.jp/contests/abc171/tasks/abc171_f)||文字列操作後のパターン数問題は「操作によって文字列Tを作ることができるか」で考察|
|[ABC173F](https://atcoder.jp/contests/abc173/tasks/abc173_f)||木の性質(木の頂点数=辺+1から木の個数=頂点数-辺数、根付きなら一次元管理可能)など利用することを考える|
|[ABC174F](https://atcoder.jp/contests/abc174/tasks/abc174_f)||クエリ毎に区間種類数問うはMo's Algorithmだが、右端でソートして、数えるべき各数の最近位置をフェニック木に載せても解ける|
|[ABC187F](https://atcoder.jp/contests/abc187/tasks/abc187_f)||部分集合の部分集合、o(3^N)のbitDP|
|[ABC189C](https://atcoder.jp/contests/abc189/tasks/abc189_c)||ヒストグラム内の最大長方形([ABC359も](https://atcoder.jp/contests/abc359/tasks/abc359_e))|
|[ABC189E](https://atcoder.jp/contests/abc189/tasks/abc189_e)||関数の合成はその関数が行列として取扱可能かまず考える。座標変換など線形な操作は行列表示可能|
|[ABC189F](https://atcoder.jp/contests/abc189/tasks/abc189_f)||漸化式が循環する場合、解をXと置いて一次方程式として表現可能かも。次数1の係数aと次数0の係数bを並行してDP|
|[ABC194E](https://atcoder.jp/contests/abc194/tasks/abc194_e)||MEXは候補側をSortedListかheapQ+Counterで保持。[ABC330Eも](https://atcoder.jp/contests/abc330/tasks/abc330_e)|
|[ABC232F](https://atcoder.jp/contests/abc232/tasks/abc232_f)||順列全探索をbitDPに落とし込む典型。遷移先をN通りとすることで乗り切るタイプ|
|[ABC235F](https://atcoder.jp/contests/abc235/tasks/abc235_f)|2129|N以下の桁DPは上限張り付きを別管理。和の場合は和とパターン数保持|
|[ABC236E](https://atcoder.jp/contests/abc236/tasks/abc236_e)|1893|平均値、中央値の最大化は解の二分探索。平均は差分和DP>=0、中央値は未満-1以上1で和DP>0|
|[ABC237E](https://atcoder.jp/contests/abc237/tasks/abc237_e)|1208|負の辺あってもポテンシャル用いてDijkstra利用可能かも|
|[ABC237F](https://atcoder.jp/contests/abc237/tasks/abc237_f)|1857|LISの進捗(最小パターン)をkey管理してDP。（その他LIS：[ABC354F](https://atcoder.jp/contests/abc354/tasks/abc354_f),[ABC360G](https://atcoder.jp/contests/abc360/tasks/abc360_g)）|
|[ABC237G](https://atcoder.jp/contests/abc237/tasks/abc237_g)|2088|繰り返しの並び替えも、参照値に対する大小で01置換すればSegTにて処理可能|
|[ABC238E](https://atcoder.jp/contests/abc238/tasks/abc238_e)|1577|問題の適切な置き換えでグラフへ|
|[ABC239F](https://atcoder.jp/contests/abc239/tasks/abc239_f)|1959|木の連結はUnionFind+マージテク|
|[ABC239G](https://atcoder.jp/contests/abc239/tasks/abc239_g)|2215|最小カットのパターン提示はカット後に残フロー計算でなく色分け|
|[ABC240F](https://atcoder.jp/contests/abc240/tasks/abc240_f)|1589|２層の階差数列は微分のイメージ(極大極小)つまり三分探索|
|[ABC241E](https://atcoder.jp/contests/abc241/tasks/abc241_e)||周期性利用問題の典型|
|[ABC241F](https://atcoder.jp/contests/abc241/tasks/abc241_f)||滑る床、無理にグラフに落とし込む必要無くBFSは可能|
|[ABC242C](https://atcoder.jp/contests/abc242/tasks/abc242_c)||辿り着ける通り数はDP、漸化式はDPか行列|
|[ABC242D](https://atcoder.jp/contests/abc242/tasks/abc242_d)||膨大な繰り返しは10\*\*7以下のパターンへの収束を見出す|
|[ABC242F](https://atcoder.jp/contests/abc242/tasks/abc242_f)||二項定理で計算量削減|
|[ABC242G](https://atcoder.jp/contests/abc242/tasks/abc242_g)||クエリ毎に区間種類数問うはMo's Algorithm[(解説)](https://strangerxxx.hateblo.jp/entry/20230314/1678795200) [(ABC293Gも)](https://atcoder.jp/contests/abc293/submissions/50656044)尺取で解ける大量のオフラインクエリはこれ|
|[ABC243E](https://atcoder.jp/contests/abc243/tasks/abc243_e)||300程まではWF法|
|[ABC243G](https://atcoder.jp/contests/abc243/tasks/abc243_g)||数列パターン数は小さい方から付け足し遷移。二個飛ばしにできるなら計算量をさらに削減|
|[ABC244D](https://atcoder.jp/contests/abc244/tasks/abc244_d)||転倒数、偶置換奇置換|
|[ABC244E](https://atcoder.jp/contests/abc244/tasks/abc244_e)||辿り着く通り数はDP|
|[ABC245E](https://atcoder.jp/contests/abc245/tasks/abc245_e)||箱選びは箱と中身を混ぜて並べる|
|[ABC245F](https://atcoder.jp/contests/abc245/tasks/abc245_f)||志向グラフのループ検出|
|[ABC246D](https://atcoder.jp/contests/abc246/tasks/abc246_d)||**○以上の満たす数でa,b決定**は片側の候補をループしてもう片側を尺取又はO(1)|
|[ABC246E](https://atcoder.jp/contests/abc246/tasks/abc246_e)||ダイクストラより早い01bfs|
|[ABC246F](https://atcoder.jp/contests/abc246/tasks/abc246_f)||N=18の場合の数は除法原理かも|
|[ABC247E](https://atcoder.jp/contests/abc247/tasks/abc247_e)||満たす区間の個数は尺取法か包除原理。coreの無い判定は別 [ABC295D](https://atcoder.jp/contests/abc295/tasks/abc295_d)|
|[ABC247F](https://atcoder.jp/contests/abc247/tasks/abc247_f)||カードの表裏に数字分散はグラフかも|
|[ABC247G](https://atcoder.jp/contests/abc247/tasks/abc247_g)||任意の数のマッチングは最小費用流問題へ|
|[ABC248C](https://atcoder.jp/contests/abc248/tasks/abc248_c)||**場合の数に見えてdpで解ける事も**。ある項までの合計数で管理|
|[ABC248F](https://atcoder.jp/contests/abc248/tasks/abc248_f)||漸化式で表せる状態変化は状態dp|
|[ABC249E](https://atcoder.jp/contests/abc249/tasks/abc249_e)||ランレングスは圧縮前と圧縮後でdp|
|[ABC250E](https://atcoder.jp/contests/abc250/tasks/abc250_e)||集合はハッシュで状態記録も可|
|[ABC250F](https://atcoder.jp/contests/abc250/tasks/abc250_f)||多角形二分割の丁度良い面積は尺取法|
|[ABC251D](https://atcoder.jp/contests/abc251/tasks/abc251_d)||構築問題、x進数を作れパズル|
|[ABC251F](https://atcoder.jp/contests/abc251/tasks/abc251_f)||残辺すべてが卑尊はDFS木、非卑尊はBFS木|
|[ABC252F](https://atcoder.jp/contests/abc252/tasks/abc252_f)||棒長結合問題は二分木のイメージ|
|[ABC253C](https://atcoder.jp/contests/abc253/tasks/abc253_c)||multiset問題はheapq管理でいけるかも、popコスト < insortコスト|
|[ABC253F](https://atcoder.jp/contests/abc253/tasks/abc253_f)||代入クエリは出力ごとに直前代入を記録|
|[ABC254D](https://atcoder.jp/contests/abc254/tasks/abc254_d)||約数内の最大平方根はエラトステネスと同要領|
|[ABC254F](https://atcoder.jp/contests/abc254/tasks/abc254_f)||クエリごとの区間解はセグメント木で管理|
|[ABC255E](https://atcoder.jp/contests/abc255/tasks/abc255_e)||漸化式変形で初項算出可能とし全探索して一番多い初項を選ぶ|
|[ABC256E](https://atcoder.jp/contests/abc256/tasks/abc256_e)||出次数1のグラフは連結成分ひとつにつき閉路1つ|
|[ABC256F](https://atcoder.jp/contests/abc256/tasks/abc256_f)||数列の累積和の累積和はある項の寄与度を計算し展開|
|[ABC257E](https://atcoder.jp/contests/abc257/tasks/abc257_e)||dpでTLEの時は桁に着目が有効なことも|
|[ABC258E](https://atcoder.jp/contests/abc258/tasks/abc258_e)||鳩の巣原理でループへ帰着する問題|
|[ABC258G](https://atcoder.jp/contests/abc258/tasks/abc258_g)||pythonでbitset|
|[ABC259F](https://atcoder.jp/contests/abc259/tasks/abc259_f)||木の取捨選択はdfsで木dp|
|[ABC260E](https://atcoder.jp/contests/abc260/tasks/abc260_e)||条件を満たす連続部分列の数は尺取法(たまに除法定理やdp)|
|[ABC260F](https://atcoder.jp/contests/abc260/tasks/abc260_f)||TLEしそうなN数でも最小数着目で鳩の巣原理で解ける|
|[ABC261E](https://atcoder.jp/contests/abc261/tasks/abc261_e)||bitごとに処理した数値を答えの配列に\|=できる|
|[ABC261F](https://atcoder.jp/contests/abc261/tasks/abc261_f)||Fenwick木は-1で復すれば再利用可能|
|[ABC262D](https://atcoder.jp/contests/abc262/tasks/abc262_d)||選ぶ項数と余りでdp|
|[ABC262E](https://atcoder.jp/contests/abc262/tasks/abc262_e)||グラフ辺の奇遇は次数の奇遇で解く|
|[ABC263E](https://atcoder.jp/contests/abc263/tasks/abc263_e)||到達期待値は末尾から計算、ゼロの処理が肝|
|[ABC264E](https://atcoder.jp/contests/abc264/tasks/abc264_e)||辺は切る処理より繋ぐ処理が楽|
|[ABC265F](https://atcoder.jp/contests/abc265/tasks/abc265_f)||累積和で計算量1オーダーダウン（**未完**)|
|[ABC267F](https://atcoder.jp/contests/abc267/tasks/abc267_f)||木の距離管理は直径の両端から|
|[ABC268D](https://atcoder.jp/contests/abc268/tasks/abc268_d)||同じものを含む順列の列挙は再帰関数で|
|[ABC268F](https://atcoder.jp/contests/abc268/tasks/abc268_f)||並べ替えの最適解はcmp関数で|
|[ABC270D](https://atcoder.jp/contests/abc270/tasks/abc270_d)||交互ターンゲームは残り石数をnと置いてdp|
|[ABC270F](https://atcoder.jp/contests/abc270/tasks/abc270_f)||多点ワープはnodeと見做す。最小全域木はクラスカル法かプラム法(ダイクストラ)|
|[ABC272G](https://atcoder.jp/contests/abc272/tasks/abc272_g)||条件満たすものを一つでも挙げるは乱択か|
|[ABC273E](https://atcoder.jp/contests/abc273/tasks/abc273_e)||リストの複数回記録と呼び出しは木構造で可能|
|[ABC278F](https://atcoder.jp/contests/abc278/tasks/abc278_f)||N=16程度の並び替えは状態DPでいけるかも|
|[ABC282E](https://atcoder.jp/contests/abc282/tasks/abc282_e)||最大全域木はunionfind+クラスカル法(グラフ不要)|
|[ABC283F](https://atcoder.jp/contests/abc283/tasks/abc283_f)||絶対値は可能ならば場合分けして外す|
|[ABC283G](https://atcoder.jp/contests/abc283/tasks/abc283_g)||xorの昇順列挙はxor基底列挙して順序を0-indexとして算出|
|[ABC286F](https://atcoder.jp/contests/abc286/tasks/abc286_f)||(中国剰余定理)互いに素な数で除した余が与えられる場合、最小公倍数以下では解が一意|
|[ABC288D](https://atcoder.jp/contests/abc288/tasks/abc288_d)||不変量を見極めて条件を単純化|
|[ABC289G](https://atcoder.jp/contests/abc289/tasks/abc289_g)||いくつかの直線から構成される最大値(最小値)はconvex_hull|
|[ABC294G](https://atcoder.jp/contests/abc294/tasks/abc294_g)||更新入る木の距離はダブリング＋オイラーツアー|
|[ABC295E](https://atcoder.jp/contests/abc295/tasks/abc295_e)||1以上M以下の確率変数Xの期待値合計∑i*p(X==i) => ∑p(X>=i)|
|[ABC296F](https://atcoder.jp/contests/abc296/tasks/abc296_f)||順番入れ替えで数列を一致させられるかは転倒数の奇遇一致次第|
|[ABC297G](https://atcoder.jp/contests/abc297/tasks/abc297_g)||多山NimはGrundy数のXORでゼロのみ後手勝ち|
|[ABC301E](https://atcoder.jp/contests/abc301/tasks/abc301_e)||N=20で最短経路長bit全探索は巡回セールスマン|
|[ABC302B](https://atcoder.jp/contests/abc302/tasks/abc302_b)||計算量が許すなら愚直に8方向探索を|
|[ABC302F](https://atcoder.jp/contests/abc302/tasks/abc302_f)||辺も頂点とみなしてみる超頂点|
|[ABC308G](https://atcoder.jp/contests/abc308/tasks/abc308_g)||集合内のXORは隣り合う数字同士が最小候補（min(x^y,y^z)<x^z)|
|[ABC309F](https://atcoder.jp/contests/abc309/tasks/abc309_f)||3要素の比較にソート+セグ木(圧座後)|
|[ABC310D](https://atcoder.jp/contests/abc310/tasks/abc310_d)||N=10で全探索は再帰で階乗かも|
|[ABC310F](https://atcoder.jp/contests/abc310/tasks/abc310_f)||20以下の集合のパターン数(確率)はbitDP|
|[ABC314E](https://atcoder.jp/contests/abc314/tasks/abc314_e)||到達期待値は末尾から計算|
|[ABC315F](https://atcoder.jp/contests/abc315/tasks/abc315_f)||制約から最低限必要な状態数を見積もる|
|[ABC317E](https://atcoder.jp/contests/abc317/tasks/abc317_e)||マップ探索はグラフ作成不要、毎クエリ4方向見るだけ|
|[ABC317F](https://atcoder.jp/contests/abc317/tasks/abc317_f)||2進数で桁DP（**未完**)|
|[ABC318F](https://atcoder.jp/contests/abc318/tasks/abc318_f)||変化座標候補を事前列挙|
|[ABC322F](https://atcoder.jp/contests/abc322/tasks/abc322_f)||モノイドセグ木|
|[ABC324F](https://atcoder.jp/contests/abc324/tasks/abc324_f)||答えの二分探索はfloatでも可|
|[ABC326F](https://atcoder.jp/contests/abc326/tasks/abc326_f)||N=40は半分全列挙|
|[ABC330F](https://atcoder.jp/contests/abc330/tasks/abc330_f)||微分で極小を求めたい時は代わりに中央値的な考え方を。左右ずらしいずれも損をする位置。[slope trickも可](https://maspypy.com/slope-trick-1-%E8%A7%A3%E8%AA%AC%E7%B7%A8)|
|[ABC331F](https://atcoder.jp/contests/abc331/tasks/abc331_f)||更新ありの回文判定はローリングハッシュ＋セグ木で|
|[ABC336E](https://atcoder.jp/contests/abc336/tasks/abc336_e)||ハーシャッド数は総和リミット決め打ちで和、余り、上限張付を別管理する桁DP|
|[ABC339D](https://atcoder.jp/contests/abc339/tasks/abc339_d)||2人の位置関係を扱う問題は組み合わせの遷移を考えることでグラフ的に解ける([ABC289E](https://atcoder.jp/contests/abc289/tasks/abc289_e))|
|[ABC339F](https://atcoder.jp/contests/abc339/tasks/abc339_f)||長大な数字も扱えはするが桁数だけの計算時間がかかるのでmodなどでシーリング|
|[ABC339G](https://atcoder.jp/contests/abc339/tasks/abc339_g)||更新の入らないオンラインクエリ区間の種類数問題はマージソート木|
|[ABC340F](https://atcoder.jp/contests/abc340/tasks/abc340_f)||一次不定方程式は拡張ユークリッド([ABC186E](https://atcoder.jp/contests/abc186/tasks/abc186_e)も)|
|[ABC346G](https://atcoder.jp/contests/abc346/tasks/abc346_g)||長方形の和集合の面積を求める|
|[ABC348F](https://atcoder.jp/contests/abc348/tasks/abc348_f)||2000^3でどれかbit演算可能そうならbitsetで通せる|
|[ABC349F](https://atcoder.jp/contests/abc349/tasks/abc349_f)||bitwise orのパターン数はゼータメビウス変換使えるかも|
|[ABC350E](https://atcoder.jp/contests/abc350/tasks/abc350_e)|1385|終わりに向けて発散のち収束する期待値はメモ化再帰で。ループの選択肢がある場合は式変形（確率ver:[ABC300E](https://atcoder.jp/contests/abc300/tasks/abc300_e)）|
|[ABC350G](https://atcoder.jp/contests/abc350/tasks/abc350_g)|2058|オンラインクエリは平方分割やマージテクなど。根付き木特有の解き方あり|
|[ABC352D](https://atcoder.jp/contests/abc352/tasks/abc352_d)||ループする側を別の等差数列に変えてみる|
|[ABC352F](https://atcoder.jp/contests/abc352/tasks/abc352_f)|2052|N=16は各点ループ＋bitDPくらい|
|[ABC353E](https://atcoder.jp/contests/abc353/tasks/abc353_e)|1217|複数文字列の最小共通接辞頭のパターン数はTrie木。[ヒストグラム内の長方形も]（http://algorithms.blog55.fc2.com/blog-entry-132.html)|
|[ABC354E](https://atcoder.jp/contests/abc354/tasks/abc354_e)|1223|交互ゲームでパターン数が2**20程度なら必勝を1と置いてbitDPも可能。勿論メモ化再帰でも解ける。|
|[ABC355F](https://atcoder.jp/contests/abc355/tasks/abc355_f)|1924|重みあり最小全域木の更新は重み上限ごとのUnionFindで減算していく|
|[ABC357E](https://atcoder.jp/contests/abc357/tasks/abc357_e)|1295|functional graphはループ内から逆算していく|
|[ABC357F](https://atcoder.jp/contests/abc357/tasks/abc357_f)|1793|モノイドセグ木ついに理解([ABC346G](https://atcoder.jp/contests/abc346/tasks/abc346_g)も併せて)|
|[ABC359D](https://atcoder.jp/contests/abc359/tasks/abc359_d)|1381|部分文字列の満たすパターン数は状態DPで一字づつ遷移|
|[ABC359E](https://atcoder.jp/contests/abc359/tasks/abc359_e)|1275|ヒストグラム内の最大長方形はsegTreeでなくstackで|
|[ABC359G](https://atcoder.jp/contests/abc359/tasks/abc359_g)|2099|木のdfsにマージテクで状態ごとの総和計算|
|[ABC360E](https://atcoder.jp/contests/abc360/tasks/abc360_e)|1249|期待値問題は確率dpも期待値dpも可能なので、楽な方で|
|[ABC361D](https://atcoder.jp/contests/abc361/tasks/abc361_d)||状態数が20以下のパズルの最適手はbitDPかBFS|
|[ABC361F](https://atcoder.jp/contests/abc361/tasks/abc361_f)|1606|べき乗パターン数問題で約数包除原理|
|[ABC362E](https://atcoder.jp/contests/abc362/tasks/abc362_e)|1225|DPの次数を削減する時は捜査の方向に気をつけて|
|[ABC362G](https://atcoder.jp/contests/abc362/tasks/abc362_g)|1625|文字列部分一致の個数をO(logN)で繰り返し判定はSuffix Array|
|[ABC363F](https://atcoder.jp/contests/abc363/tasks/abc363_f)|1913|限りなく全探索に近い生成系は再帰＋枝刈りが勝負|
|[ABC364F](https://atcoder.jp/contests/abc364/tasks/abc364_f)|1878|隣との非結合を1と置けばsegTで集合の個数を求められる。[(ABC356Fも)](https://atcoder.jp/contests/abc356/tasks/abc356_f)|
|[ABC366E](https://atcoder.jp/contests/abc366/tasks/abc366_e)|1515|マンハッタン距離は XY別々で片側ループ or 45°回転|
|[ABC367F](https://atcoder.jp/contests/abc367/tasks/abc367_f)|1540|集合の一致はHashで判定(Zobrist hash)|
|[ABC368E](https://atcoder.jp/contests/abc368/tasks/abc368_e)|2140|時系列はグラフで無理そうならイベント(ソート)で|
|[ABC368G](https://atcoder.jp/contests/abc368/tasks/abc368_g)|1841|無理に見えるアルゴリズムも制約の関係から愚直でOKな場合がある|
|[ABC370E](https://atcoder.jp/contests/abc370/tasks/abc370_e)||dpは式表記したうえで計算量改善のため変形|

## 典型90問
- [最少数え上げ要素を選択#25](https://atcoder.jp/contests/typical90/submissions/35225706)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/025.jpg)）
- [答え側を2分探索#1](https://atcoder.jp/contests/typical90/submissions/34487062)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/001.jpg)）
- [半分全探索＋2分探索#51](https://atcoder.jp/contests/typical90/submissions/36008121)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/051.jpg)）
- [円環はlistにして複製連結で二分探索可能に#76](https://atcoder.jp/contests/typical90/submissions/38541165)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/076.jpg)）
- [ダブリング(根付き木)#35](https://atcoder.jp/contests/typical90/submissions/35368779)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/035-02.jpg)）
- [桁DP#5](https://atcoder.jp/contests/typical90/submissions/33173921)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/005-01.jpg)）
- [部分集合はbitDP#45](https://atcoder.jp/contests/typical90/submissions/35441720)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/045.jpg)）
- [部分集合の場合の数は状態DP#8](https://atcoder.jp/contests/typical90/submissions/34868209)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg)）
- [時限タスクは締切sortタスクx時間DP#11](https://atcoder.jp/contests/typical90/submissions/34888277)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/011-02.jpg)）
- [数列操作は区間DP#19](https://atcoder.jp/contests/typical90/submissions/35210132)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/019.jpg)）
- [木パターンの数え上げは木DP#73](https://atcoder.jp/contests/typical90/submissions/38537528)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/073.jpg)）
- [辞書順は貪欲法#6](https://atcoder.jp/contests/typical90/submissions/34867193)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/006.jpg)）
- [連結判定はUnionFind#12](https://atcoder.jp/contests/typical90/submissions/34889083)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/012.jpg)）
- [最少全域木はUnionFind+クラスカル法#49](https://atcoder.jp/contests/typical90/submissions/35992502)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/049.jpg)）
- [加算と総和を繰返すにはFenwickTree#17](https://atcoder.jp/contests/typical90/submissions/35192768)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/017-03.jpg)）
- [更新と取得を繰返すにはSegmentTree#29#37](https://atcoder.jp/contests/typical90/submissions/35241803)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/029-02.jpg)）
- [素因数列挙はエラトステネスで非素数への加算#30](https://atcoder.jp/contests/typical90/submissions/35241997)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/030.jpg)）
- [各桁の数字の和＝Kの通り数は単調DP#42](https://atcoder.jp/contests/typical90/submissions/35427310)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/042.jpg)）
- [XOR問題や順番を問わない数列操作は掃き出し法#57](https://atcoder.jp/contests/typical90/submissions/36314716)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/057.jpg)）
- [bit演算で64倍高速化#59](https://atcoder.jp/contests/typical90/submissions/36357617)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/059-02.jpg)）
- [交互ゲームはgrundy数/dp/貪欲法#31](https://atcoder.jp/contests/typical90/submissions/35243279)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/031.jpg)）
- [連続区間は尺取法(単調増加なら二分探索も)#34](https://atcoder.jp/contests/typical90/submissions/35245981)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/034.jpg)）
- [マンハッタン距離は45度回転#36](https://atcoder.jp/contests/typical90/submissions/35370438)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/036.jpg)）
- [絶対値最小は中央値#70](https://atcoder.jp/contests/typical90/submissions/37367857)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/070.jpg)）
- [根付き木の距離は部下の数#39](https://atcoder.jp/contests/typical90/submissions/35374640)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/039.jpg)）
- [凸包×Pickの定理#41](https://atcoder.jp/contests/typical90/submissions/35426880)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/041-03.jpg)）
- [燃やす埋める問題は最大フロー#40](https://atcoder.jp/contests/typical90/submissions/35389500)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/040.jpg)）
- [文字列一致判定はローリングハッシュ#47](https://atcoder.jp/contests/typical90/submissions/35620637)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/047-02.jpg)）
- [完全結合の部分は点を追加することで辺数を削減可能#54](https://atcoder.jp/contests/typical90/submissions/36189224)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/054.jpg)）
- [ループ(周期性)検出で繰り返し削減#58](https://atcoder.jp/contests/typical90/submissions/36319380)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/058.jpg)）
- [最長増加部分列(LIS)アルゴリズム#60](https://atcoder.jp/contests/typical90/submissions/36358194)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/060.jpg)）
- [クエリ先読み#68](https://atcoder.jp/contests/typical90/submissions/37317678)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/068.jpg)）
- [一方通行のルート探索はトポロジカルソート(閉路検出も)#71](https://atcoder.jp/contests/typical90/submissions/38447554)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/071-03.jpg)）
- [余事象の組み合わせは包除原理#80](https://atcoder.jp/contests/typical90/submissions/38682064)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/080.jpg)）
