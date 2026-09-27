# FileUpload

元のフォルダ: `src/components/FileUpload/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: FileUpload.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';
import { createPortal } from 'react-dom';

export type FileUploadProps = ComponentProps<'div'> & {
  maxFiles?: number;
  hasError?: boolean;
  droppable?: boolean;
};

export const FileUpload = (props: FileUploadProps) => {
  const { children, className, maxFiles = 1, hasError = false, droppable = false, ...rest } = props;

  const isMultiple = maxFiles > 1;

  return (
    <div
      className={`
        group/file-upload
        text-solid-gray-800 text-std-16N-170 [overflow-wrap:anywhere]
        ${className ?? ''}
      `}
      data-multiple={isMultiple ? 'true' : 'false'}
      data-has-error={hasError ? 'true' : undefined}
      data-droppable={droppable ? 'true' : undefined}
      {...rest}
    >
      {children}
    </div>
  );
};

export type FileUploadInputProps = Omit<ComponentProps<'input'>, 'type'>;

export const FileUploadInput = forwardRef<HTMLInputElement, FileUploadInputProps>((props, ref) => {
  const { className, ...rest } = props;

  return (
    <input
      ref={ref}
      type='file'
      className={`
        hidden
        ${className ?? ''}
      `}
      {...rest}
    />
  );
});

export type FileUploadDropAreaProps = ComponentProps<'div'> & {
  isDragOver?: boolean;
};

export const FileUploadDropArea = (props: FileUploadDropAreaProps) => {
  const { children, className, isDragOver = false, ...rest } = props;

  return (
    <div
      className={`
        group/drop-area
        rounded-8 p-8 border border-solid-gray-536 bg-solid-gray-50
        group-data-[has-error=true]/file-upload:border-error-1
        data-[dragover=true]:outline data-[dragover=true]:outline-4 data-[dragover=true]:outline-success-1 data-[dragover=true]:-outline-offset-4 data-[dragover=true]:bg-green-50
        ${className ?? ''}
      `}
      data-dragover={isDragOver ? 'true' : undefined}
      {...rest}
    >
      {children}
    </div>
  );
};

export type FileUploadFileListProps = ComponentProps<'ul'>;

export const FileUploadFileList = (props: FileUploadFileListProps) => {
  const { children, className, ...rest } = props;

  return (
    <ul
      className={`
        mt-4 p-0 list-none [counter-reset:file-item]
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
    </ul>
  );
};

export type FileUploadFileItemProps = ComponentProps<'li'> & {
  hasError?: boolean;
};

export const FileUploadFileItem = (props: FileUploadFileItemProps) => {
  const { children, className, hasError = false, ...rest } = props;

  return (
    <li
      className={`
        group/file-item
        flex items-baseline [counter-increment:file-item]
        [&+&]:mt-1
        ${className ?? ''}
      `}
      data-error={hasError ? 'true' : undefined}
      {...rest}
    >
      {children}
    </li>
  );
};

export type FileUploadFileMarkerProps = ComponentProps<'div'>;

export const FileUploadFileMarker = (props: FileUploadFileMarkerProps) => {
  const { className, ...rest } = props;

  return (
    <div
      className={`
        shrink-0
        group-data-[multiple=true]/file-upload:w-8
        group-data-[multiple=true]/file-upload:before:content-[counter(file-item)'.']
        group-data-[multiple=false]/file-upload:flex group-data-[multiple=false]/file-upload:self-start group-data-[multiple=false]/file-upload:justify-center group-data-[multiple=false]/file-upload:items-center group-data-[multiple=false]/file-upload:w-6 group-data-[multiple=false]/file-upload:h-[calc(30/16*1rem)]
        group-data-[multiple=false]/file-upload:before:w-1.5 group-data-[multiple=false]/file-upload:before:h-1.5 group-data-[multiple=false]/file-upload:before:rounded-full group-data-[multiple=false]/file-upload:before:bg-current group-data-[multiple=false]/file-upload:before:content-['']
        group-data-[multiple=false]/file-upload:forced-colors:before:bg-[CanvasText]
        ${className ?? ''}
      `}
      {...rest}
    />
  );
};

export type FileUploadFileInfoProps = ComponentProps<'div'>;

export const FileUploadFileInfo = (props: FileUploadFileInfoProps) => {
  const { children, className, ...rest } = props;

  return (
    <div
      className={`
        flex-1 min-w-0
        group-data-[error=true]/file-item:border-l-4 group-data-[error=true]/file-item:border-error-1 group-data-[error=true]/file-item:pl-2 group-data-[error=true]/file-item:text-error-1
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
    </div>
  );
};

export type FileUploadFileNameProps = ComponentProps<'span'>;

export const FileUploadFileName = (props: FileUploadFileNameProps) => {
  const { children, className, ...rest } = props;

  return (
    <span className={`mr-4 font-bold ${className ?? ''}`} {...rest}>
      {children}
    </span>
  );
};

export type FileUploadFileMetaProps = ComponentProps<'span'>;

export const FileUploadFileMeta = (props: FileUploadFileMetaProps) => {
  const { children, className, ...rest } = props;

  return (
    <span
      className={`
        text-solid-gray-600
        group-data-[error=true]/file-item:text-inherit
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
    </span>
  );
};

export type FileUploadViewportOverlayProps = ComponentProps<'div'>;

export const FileUploadViewportOverlay = (props: FileUploadViewportOverlayProps) => {
  const { children, className, ...rest } = props;

  if (typeof document === 'undefined') {
    return null;
  }

  return createPortal(
    <div
      className={`
        fixed inset-0 z-[9999] border-4 border-success-1 bg-green-50
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
    </div>,
    document.body,
  );
};

export type FileUploadViewportOverlayMessageProps = ComponentProps<'div'>;

export const FileUploadViewportOverlayMessage = (props: FileUploadViewportOverlayMessageProps) => {
  const { children, className, ...rest } = props;

  return (
    <div
      className={`
        flex justify-center content-center flex-wrap box-border w-full h-full p-[calc(2rem-4px)]
        text-[clamp(calc(18/16*1rem),0.75rem+1.875vw,calc(48/16*1rem))] font-bold pointer-events-none
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
    </div>
  );
};
````

<!-- file: hooks/index.ts -->
````ts
export type { UseFileDropOptions } from './useFileDrop';
export { useFileDrop } from './useFileDrop';
export type { UseFileStateOptions } from './useFileState';
export { useFileState } from './useFileState';
export type { UseFileUploadOptions } from './useFileUpload';
export { useFileUpload } from './useFileUpload';
````

<!-- file: hooks/useFileDrop.ts -->
````ts
import { type DragEvent, type RefObject, useEffect, useRef, useState } from 'react';
import { fileUploadDefaultMessages } from '../messages';
import type { FileUploadMessages } from '../types';

export type UseFileDropOptions = {
  /** ドラッグ＆ドロップを有効化 */
  droppable?: boolean;
  /** 全画面ドロップエリアを有効化 */
  dropAreaExpandable?: boolean;
  /** ファイル追加時のコールバック */
  onFilesAdded: (files: File[]) => void;
  /** フォーカスを戻すためのref */
  focusTargetRef?: RefObject<HTMLElement | null>;
  /** カスタムメッセージ */
  messages?: FileUploadMessages;
};

// 全画面ドロップエリアの排他制御用
const expandedDropAreaState = {
  activeCallback: null as (() => void) | null,
};

const registerExpandedDropArea = (callback: () => void) => {
  if (expandedDropAreaState.activeCallback && expandedDropAreaState.activeCallback !== callback) {
    expandedDropAreaState.activeCallback();
  }
  expandedDropAreaState.activeCallback = callback;
};

const unregisterExpandedDropArea = (callback: () => void) => {
  if (expandedDropAreaState.activeCallback === callback) {
    expandedDropAreaState.activeCallback = null;
  }
};

export const useFileDrop = (options: UseFileDropOptions) => {
  const {
    dropAreaExpandable = false,
    onFilesAdded,
    focusTargetRef,
    messages: customMessages,
  } = options;

  const messages = customMessages ?? fileUploadDefaultMessages;

  const [isDragOver, setIsDragOver] = useState(false);
  const [isExpandedDropArea, setIsExpandedDropArea] = useState(false);
  const [showViewportOverlay, setShowViewportOverlay] = useState(false);
  const [announcerText, setAnnouncerText] = useState('');
  const [announcerAssertiveText, setAnnouncerAssertiveText] = useState('');

  const dragCounterRef = useRef(0);
  const announcerTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const dragOverTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const dropAnnounceIntervalRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const collapseCallbackRef = useRef(() => setIsExpandedDropArea(false));

  const announceText = (text: string, assertive = false) => {
    if (announcerTimerRef.current) {
      clearTimeout(announcerTimerRef.current);
    }

    const setText = assertive ? setAnnouncerAssertiveText : setAnnouncerText;

    setText('');
    announcerTimerRef.current = setTimeout(() => {
      setText(text);
      announcerTimerRef.current = setTimeout(() => {
        setText('');
      }, 1000);
    }, 100);
  };

  const stopDropAnnounce = () => {
    if (dropAnnounceIntervalRef.current) {
      clearInterval(dropAnnounceIntervalRef.current);
      dropAnnounceIntervalRef.current = null;
    }
  };

  const startDropAnnounce = () => {
    stopDropAnnounce();
    const message = messages.announce.dropAvailable;
    announceText(message, true);

    dropAnnounceIntervalRef.current = setInterval(() => {
      announceText(message);
    }, 3000);
  };

  const handleExpandedDropAreaChange = (checked: boolean) => {
    setIsExpandedDropArea(checked);
    if (checked) {
      registerExpandedDropArea(collapseCallbackRef.current);
    } else {
      unregisterExpandedDropArea(collapseCallbackRef.current);
    }
  };

  // ドロップエリア用ハンドラ
  const handleDragEnter = () => {
    dragCounterRef.current++;
    if (dragCounterRef.current === 1) {
      setIsDragOver(true);
      startDropAnnounce();
    }
  };

  const handleDragOver = (e: DragEvent) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy';
  };

  const handleDragLeave = () => {
    dragCounterRef.current--;
    if (dragCounterRef.current === 0) {
      setIsDragOver(false);
      stopDropAnnounce();
      announceText(messages.announce.dropUnavailable, true);
    }
  };

  const handleDrop = (e: DragEvent) => {
    e.preventDefault();
    dragCounterRef.current = 0;
    setIsDragOver(false);
    stopDropAnnounce();

    const fileList = Array.from(e.dataTransfer?.files || []);
    onFilesAdded(fileList);
    focusTargetRef?.current?.focus();
  };

  // ビューポートオーバーレイ用ハンドラ
  const handleViewportDragEnter = () => {
    dragCounterRef.current++;
    if (dragCounterRef.current === 1) {
      startDropAnnounce();
    }
  };

  const handleViewportDragOver = (e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    e.dataTransfer.dropEffect = 'copy';

    if (dragOverTimerRef.current) {
      clearTimeout(dragOverTimerRef.current);
    }

    dragOverTimerRef.current = setTimeout(() => {
      if (showViewportOverlay) {
        dragCounterRef.current = 0;
        setShowViewportOverlay(false);
      }
    }, 300);
  };

  const handleViewportDragLeave = () => {
    dragCounterRef.current--;
    if (dragCounterRef.current === 0) {
      setShowViewportOverlay(false);
      stopDropAnnounce();
      announceText(messages.announce.dropUnavailable, true);
    }
  };

  const handleViewportDrop = (e: DragEvent) => {
    e.preventDefault();
    dragCounterRef.current = 0;
    setShowViewportOverlay(false);
    stopDropAnnounce();

    const fileList = Array.from(e.dataTransfer?.files || []);
    onFilesAdded(fileList);
    focusTargetRef?.current?.focus();
  };

  // ドキュメント全体のドラッグオーバーイベント
  useEffect(() => {
    if (!dropAreaExpandable) return;

    const handleDocumentDragOver = (e: globalThis.DragEvent) => {
      if (isExpandedDropArea) {
        e.preventDefault();
        setShowViewportOverlay(true);
      }
    };

    document.documentElement.addEventListener('dragover', handleDocumentDragOver);
    return () => {
      document.documentElement.removeEventListener('dragover', handleDocumentDragOver);
    };
  }, [dropAreaExpandable, isExpandedDropArea]);

  // クリーンアップ
  // biome-ignore lint/correctness/useExhaustiveDependencies: クリーンアップは初回マウント時のみ実行
  useEffect(() => {
    return () => {
      if (announcerTimerRef.current) {
        clearTimeout(announcerTimerRef.current);
      }
      if (dragOverTimerRef.current) {
        clearTimeout(dragOverTimerRef.current);
      }
      stopDropAnnounce();
      // 全画面ドロップエリアの登録解除
      unregisterExpandedDropArea(collapseCallbackRef.current);
    };
  }, []);

  return {
    // State
    isDragOver,
    isExpandedDropArea,
    showViewportOverlay,
    announcerText,
    announcerAssertiveText,

    // Handlers
    handleExpandedDropAreaChange,

    // Drop area handlers
    handleDragEnter,
    handleDragOver,
    handleDragLeave,
    handleDrop,

    // Viewport overlay handlers
    handleViewportDragEnter,
    handleViewportDragOver,
    handleViewportDragLeave,
    handleViewportDrop,
  };
};
````

<!-- file: hooks/useFileState.ts -->
````ts
import { type ChangeEvent, useRef, useState } from 'react';
import { fileUploadDefaultMessages } from '../messages';
import type { FileInfo, FileUploadMessages } from '../types';
import { isFileTypeAllowed, parseAcceptAttribute, parseSize } from '../utils';

export type UseFileStateOptions = {
  /** 選択可能なファイル数の上限 */
  maxFiles?: number;
  /** 1ファイルあたりの最大サイズ（例: "5MB"） */
  maxFileSize?: string;
  /** 合計の最大サイズ（例: "10MB"） */
  maxTotalSize?: string;
  /** 許可するファイル形式（accept属性形式） */
  accept?: string;
  /** 初期ファイル一覧 */
  initialFiles?: FileInfo[];
  /** カスタムメッセージ */
  messages?: FileUploadMessages;
};

export const useFileState = (options: UseFileStateOptions = {}) => {
  const {
    maxFiles = 1,
    maxFileSize,
    maxTotalSize,
    accept = '',
    initialFiles = [],
    messages: customMessages,
  } = options;

  const messages = customMessages ?? fileUploadDefaultMessages;

  const [files, setFiles] = useState<FileInfo[]>(initialFiles);
  const [errors, setErrors] = useState<string[]>([]);

  const inputRef = useRef<HTMLInputElement>(null);
  const selectButtonRef = useRef<HTMLButtonElement>(null);

  const maxFileSizeBytes = maxFileSize ? parseSize(maxFileSize) : null;
  const maxTotalSizeBytes = maxTotalSize ? parseSize(maxTotalSize) : null;
  const totalSize = files.reduce((sum, f) => sum + f.size, 0);
  const hasError = errors.length > 0;
  const isMultiple = maxFiles > 1;

  // VoiceOver + Safari でaria-describedbyのキャッシュ問題を回避するためのキー
  // 選択ファイルサマリー要素のIDサフィックスとして使用することで、変更時にIDが変わりキャッシュが無効化される
  const selectionSummarySuffix = `${files.length}-${totalSize}`;

  const validateFiles = (
    fileList: FileInfo[],
  ): { errors: string[]; validatedFiles: FileInfo[] } => {
    const newErrors: string[] = [];
    const validatedFiles = fileList.map((f) => ({
      ...f,
      errors: f.isExisting ? f.errors : [],
    }));

    const newFiles = validatedFiles.filter((f) => !f.isExisting);

    if (fileList.length > maxFiles) {
      newErrors.push(messages.error.maxFiles);
    }

    const allowedExtensions = parseAcceptAttribute(accept);
    const fileTotalSize = fileList.reduce((sum, f) => sum + (f.size || 0), 0);

    newFiles.forEach((fileInfo) => {
      if (allowedExtensions.length > 0 && fileInfo.file) {
        const mimeType = fileInfo.file.type;

        if (!isFileTypeAllowed(fileInfo.name, mimeType, allowedExtensions)) {
          fileInfo.errors = fileInfo.errors || [];
          fileInfo.errors.push(messages.error.invalidType);
        }
      }

      if (maxFileSizeBytes !== null && fileInfo.size > maxFileSizeBytes) {
        fileInfo.errors = fileInfo.errors || [];
        fileInfo.errors.push(messages.error.maxFileSize);
      }
    });

    if (maxTotalSizeBytes !== null && fileTotalSize > maxTotalSizeBytes) {
      newErrors.push(messages.error.maxTotalSize);
    }

    const hasFileErrors = validatedFiles.some((f) => f.errors && f.errors.length > 0);
    if (hasFileErrors) {
      newErrors.unshift(messages.error.hasFileErrors);
    }

    return { errors: newErrors, validatedFiles };
  };

  const addFiles = (newFileList: File[]) => {
    const filesToAdd = isMultiple ? newFileList : newFileList.slice(0, 1);

    // 単一ファイルモードで既存ファイルがある場合は置き換え
    const existingFiles = !isMultiple && files.length > 0 ? [] : files;

    const newFiles: FileInfo[] = filesToAdd.map((file) => ({
      id: `file-${Math.random().toString(36).slice(-8)}`,
      file: file,
      name: file.name,
      size: file.size,
      isExisting: false,
      errors: [],
    }));

    const updatedFiles = [...existingFiles, ...newFiles];
    const { errors: newErrors, validatedFiles } = validateFiles(updatedFiles);
    setFiles(validatedFiles);
    setErrors(newErrors);
  };

  const removeFile = (fileId: string, index: number) => {
    const updatedFiles = files.filter((f) => f.id !== fileId);
    const { errors: newErrors, validatedFiles } = validateFiles(updatedFiles);
    setFiles(validatedFiles);
    setErrors(newErrors);

    if (updatedFiles.length === 0) {
      selectButtonRef.current?.focus();
    } else if (index < updatedFiles.length) {
      const nextButton = document.getElementById(`${updatedFiles[index].id}-remove`);
      nextButton?.focus();
    } else {
      const lastButton = document.getElementById(
        `${updatedFiles[updatedFiles.length - 1].id}-remove`,
      );
      lastButton?.focus();
    }
  };

  const handleSelectButtonClick = () => {
    inputRef.current?.click();
  };

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    const fileList = Array.from(e.target.files || []);
    addFiles(fileList);
    if (inputRef.current) {
      inputRef.current.value = '';
    }
    selectButtonRef.current?.focus();
  };

  return {
    // State
    files,
    errors,
    totalSize,
    hasError,
    isMultiple,
    maxFileSizeBytes,
    maxTotalSizeBytes,
    selectionSummarySuffix,

    // Refs
    inputRef,
    selectButtonRef,

    // Actions
    setFiles,
    setErrors,
    addFiles,
    removeFile,
    validateFiles,

    // Handlers
    handleSelectButtonClick,
    handleInputChange,

    // Messages
    messages,
  };
};
````

<!-- file: hooks/useFileUpload.ts -->
````ts
import type { FileInfo, FileUploadMessages } from '../types';
import { useFileDrop } from './useFileDrop';
import { useFileState } from './useFileState';

export type UseFileUploadOptions = {
  /** 選択可能なファイル数の上限 */
  maxFiles?: number;
  /** 1ファイルあたりの最大サイズ（例: "5MB"） */
  maxFileSize?: string;
  /** 合計の最大サイズ（例: "10MB"） */
  maxTotalSize?: string;
  /** 許可するファイル形式（accept属性形式） */
  accept?: string;
  /** ドラッグ＆ドロップを有効化 */
  droppable?: boolean;
  /** 全画面ドロップエリアを有効化 */
  dropAreaExpandable?: boolean;
  /** 初期ファイル一覧 */
  initialFiles?: FileInfo[];
  /** カスタムメッセージ */
  messages?: FileUploadMessages;
};

export const useFileUpload = (options: UseFileUploadOptions = {}) => {
  const {
    maxFiles,
    maxFileSize,
    maxTotalSize,
    accept,
    droppable = false,
    dropAreaExpandable = false,
    initialFiles,
    messages,
  } = options;

  const fileState = useFileState({
    maxFiles,
    maxFileSize,
    maxTotalSize,
    accept,
    initialFiles,
    messages,
  });

  const fileDrop = useFileDrop({
    droppable,
    dropAreaExpandable,
    onFilesAdded: fileState.addFiles,
    focusTargetRef: fileState.selectButtonRef,
    messages,
  });

  return {
    // From useFileState
    files: fileState.files,
    errors: fileState.errors,
    totalSize: fileState.totalSize,
    hasError: fileState.hasError,
    isMultiple: fileState.isMultiple,
    maxFileSizeBytes: fileState.maxFileSizeBytes,
    maxTotalSizeBytes: fileState.maxTotalSizeBytes,
    selectionSummarySuffix: fileState.selectionSummarySuffix,
    inputRef: fileState.inputRef,
    selectButtonRef: fileState.selectButtonRef,
    setFiles: fileState.setFiles,
    setErrors: fileState.setErrors,
    addFiles: fileState.addFiles,
    removeFile: fileState.removeFile,
    validateFiles: fileState.validateFiles,
    handleSelectButtonClick: fileState.handleSelectButtonClick,
    handleInputChange: fileState.handleInputChange,
    messages: fileState.messages,

    // From useFileDrop
    isDragOver: fileDrop.isDragOver,
    isExpandedDropArea: fileDrop.isExpandedDropArea,
    showViewportOverlay: fileDrop.showViewportOverlay,
    announcerText: fileDrop.announcerText,
    announcerAssertiveText: fileDrop.announcerAssertiveText,
    handleExpandedDropAreaChange: fileDrop.handleExpandedDropAreaChange,
    handleDragEnter: fileDrop.handleDragEnter,
    handleDragOver: fileDrop.handleDragOver,
    handleDragLeave: fileDrop.handleDragLeave,
    handleDrop: fileDrop.handleDrop,
    handleViewportDragEnter: fileDrop.handleViewportDragEnter,
    handleViewportDragOver: fileDrop.handleViewportDragOver,
    handleViewportDragLeave: fileDrop.handleViewportDragLeave,
    handleViewportDrop: fileDrop.handleViewportDrop,
  };
};
````

<!-- file: index.ts -->
````ts
export {
  FileUpload,
  FileUploadDropArea,
  FileUploadFileInfo,
  FileUploadFileItem,
  FileUploadFileList,
  FileUploadFileMarker,
  FileUploadFileMeta,
  FileUploadFileName,
  FileUploadInput,
  FileUploadViewportOverlay,
  FileUploadViewportOverlayMessage,
} from './FileUpload';
export { useFileUpload } from './hooks';
export { fileUploadDefaultMessages } from './messages';
export type { FileInfo, FileUploadMessages } from './types';
````

<!-- file: messages.ts -->
````ts
import type { FileUploadMessages } from './types';

export const fileUploadDefaultMessages: FileUploadMessages = {
  error: {
    maxFiles: '選択できるファイル数が上限を超過しています。',
    maxTotalSize: '選択できるファイルサイズの合計が上限を超過しています。',
    invalidType: '許可されていないファイル形式です。',
    maxFileSize: 'ファイルサイズが上限を超過しています。',
    hasFileErrors: '選択したファイルにエラーがあります。該当ファイルをチェックしてください。',
  },
  announce: {
    dropAvailable: 'ここにドロップできます。',
    dropUnavailable: 'ドロップエリア外。',
  },
};
````

<!-- file: types.ts -->
````ts
export type FileInfo = {
  id: string;
  name: string;
  size: number;
  file?: File;
  isExisting?: boolean;
  errors?: string[];
};

export type FileUploadMessages = {
  error: {
    maxFiles: string;
    maxTotalSize: string;
    invalidType: string;
    maxFileSize: string;
    hasFileErrors: string;
  };
  announce: {
    dropAvailable: string;
    dropUnavailable: string;
  };
};
````

<!-- file: utils/formatSize.ts -->
````ts
export const formatSize = (bytes: number, precision: number | null = null): string => {
  if (bytes === 0) return '0B';

  const units = ['B', 'KB', 'MB', 'GB'];
  const k = 1024;
  const i = Math.min(Math.floor(Math.log(bytes) / Math.log(k)), units.length - 1);

  const decimals = precision !== null ? precision : i > 0 ? 1 : 0;
  return `${parseFloat((bytes / k ** i).toFixed(decimals))}${units[i]}`;
};
````

<!-- file: utils/index.ts -->
````ts
export { formatSize } from './formatSize';
export { isFileTypeAllowed } from './isFileTypeAllowed';
export { parseAcceptAttribute } from './parseAcceptAttribute';
export { parseSize } from './parseSize';
````

<!-- file: utils/isFileTypeAllowed.ts -->
````ts
const getFileExtension = (filename: string): string => {
  const match = filename.match(/\.([^.]+)$/);
  return match ? `.${match[1].toLowerCase()}` : '';
};

export const isFileTypeAllowed = (
  filename: string,
  mimeType: string,
  allowedExtensions: string[],
): boolean => {
  const ext = getFileExtension(filename);

  return allowedExtensions.some((allowed) => {
    if (allowed.includes('/*')) {
      const [category] = allowed.split('/');
      return mimeType.startsWith(`${category}/`);
    }
    if (allowed.startsWith('.')) {
      return ext === allowed;
    }
    return mimeType === allowed;
  });
};
````

<!-- file: utils/parseAcceptAttribute.ts -->
````ts
export const parseAcceptAttribute = (accept: string): string[] => {
  if (!accept) return [];
  return accept.split(',').map((s) => s.trim().toLowerCase());
};
````

<!-- file: utils/parseSize.ts -->
````ts
export const parseSize = (sizeStr: string | null): number | null => {
  if (!sizeStr) return null;

  const units: Record<string, number> = {
    b: 1,
    kb: 1024,
    mb: 1024 * 1024,
    gb: 1024 * 1024 * 1024,
  };

  const match = sizeStr.toLowerCase().match(/^(\d+(?:\.\d+)?)\s*(b|kb|mb|gb)?$/);
  if (!match) return null;

  const value = parseFloat(match[1]);
  const unit = match[2] || 'b';

  return Math.floor(value * units[unit]);
};
````
