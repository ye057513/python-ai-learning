JsonOutputParser vs PydanticOutputParser 的区别和使用场景
    JsonOutputParser输出格式为JSON字符串，PydanticOutputParser输出格式为Python对象
    根据场景选择不同的OutputParser
stream() 和 invoke() 的区别，什么时候用哪个
    stream() 用于异步输出，invoke() 用于同步输出
    当需要实时输出时，使用 stream()
    stream() 用于处理大文件，invoke() 用于处理小文件
    一个是遇到可以直接小定义的文件时就用invoke()
    一个遇到量大，数据较为复杂时就用stream()
temperature=0 为什么在结构化输出场景下必须设置
    结构化输出场景下，模型的输出必须符合特定的格式，不能包含随机元素
    因此，必须设置 temperature=0 来确保模型的输出符合要求
    也就是要确定数据以及输出结果的真实性
